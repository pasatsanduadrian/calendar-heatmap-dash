import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from pyngrok import ngrok
import threading

# ---------------------------
# Load .env variables
# ---------------------------
load_dotenv()
excel_path = os.getenv("EXCEL_PATH", "cal.xlsx")
ngrok_token = os.getenv("NGROK_TOKEN")
ngrok_hostname = os.getenv("NGROK_HOSTNAME", "")
PORT = int(os.getenv("PORT", 5002))

# ---------------------------
# Data loading and preprocessing
# ---------------------------
def prepare_calendar_data(excel_path, sheet_name="Sheet1", start_column="dtstart"):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df[start_column] = pd.to_datetime(df[start_column], errors='coerce')
    df = df.dropna(subset=[start_column])
    df['date_only'] = df[start_column].dt.date
    # Count events per day
    day_counts = df['date_only'].value_counts().sort_index()
    calendar_df = pd.DataFrame({'date': day_counts.index, 'count': day_counts.values})
    calendar_df['year'] = pd.DatetimeIndex(calendar_df['date']).year
    calendar_df['month'] = pd.DatetimeIndex(calendar_df['date']).month
    calendar_df['day'] = pd.DatetimeIndex(calendar_df['date']).day
    return calendar_df

calendar_df = prepare_calendar_data(excel_path)
available_years = sorted(calendar_df['year'].unique())

# ---------------------------
# Heatmap function
# ---------------------------
def make_calendar_heatmap(df, selected_year):
    data = df[df['year'] == selected_year]
    z = np.zeros((12, 31))
    for _, row in data.iterrows():
        z[row['month']-1, row['day']-1] = row['count']
    months = ['Ian', 'Feb', 'Mar', 'Apr', 'Mai', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days = list(range(1, 32))
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=days,
        y=months,
        hoverongaps=False,
        colorscale='YlGn',
        colorbar=dict(title="Nr. evenimente"),
        hovertemplate="Luna %{y}, Ziua %{x}: %{z} evenimente<extra></extra>"
    ))
    fig.update_layout(
        title=f"Heatmap calendaristic interactiv — {selected_year}",
        xaxis_title="Ziua",
        yaxis_title="Luna",
        xaxis_nticks=31,
        yaxis_nticks=12,
        margin=dict(l=50, r=50, t=60, b=50),
        autosize=True,
        height=500,
    )
    return fig

# ---------------------------
# Dash App
# ---------------------------
app = Dash(__name__)
app.layout = html.Div([
    html.H2("Calendar Heatmap — Selectează anul"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in available_years],
        value=available_years[0],
        clearable=False,
        style={'width': '200px'}
    ),
    dcc.Graph(id='calendar-heatmap', config={'displayModeBar': False}),
    html.Div("🛈 Folosește mouse hover pentru a vedea valorile exacte pe fiecare zi.", style={'marginTop': '15px', 'fontSize': '14px', 'color': '#333'}),
    html.Div(f"Accesează această pagină la adresa: https://{ngrok_hostname}" if ngrok_hostname else "", style={'marginTop': '30px', 'fontSize': '13px', 'color': '#aaa'}),
], style={'padding': '32px'})

@app.callback(
    Output('calendar-heatmap', 'figure'),
    Input('year-dropdown', 'value')
)
def update_heatmap(selected_year):
    return make_calendar_heatmap(calendar_df, selected_year)

# ---------------------------
# Run server and ngrok
# ---------------------------
def main():
    if ngrok_token:
        ngrok.set_auth_token(ngrok_token)
        try:
            if ngrok_hostname:
                public_url = ngrok.connect(PORT, hostname=ngrok_hostname)
            else:
                public_url = ngrok.connect(PORT)
        except Exception as e:
            print("Eroare la conectarea cu hostname static:", e)
            public_url = ngrok.connect(PORT)
        print(f"LINK PAGINĂ WEB: {public_url.public_url}")

    def run_app():
        app.run(host='0.0.0.0', port=PORT, debug=False)

    thread = threading.Thread(target=run_app)
    thread.daemon = True
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
