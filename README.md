# 📅 Calendar Heatmap Dash App

Aplicație Dash/Python pentru generarea și vizualizarea unui heatmap calendaristic interactiv (stil GitHub), pe baza datelor dintr-un fișier Excel cu evenimente zilnice.

---

## ⚡️ Funcționalități

- Selectare rapidă a anului (dropdown).
- Heatmap interactiv cu hover/tooltip pe fiecare zi (plotly).
- Pagina web accesibilă public via ngrok (link static sau dinamic).
- Configurare ușoară pentru propriul tău fișier Excel.

---

## 🚀 Testare rapidă în Google Colab

**Folosește celula de mai jos pentru a testa direct aplicația cu un fișier de exemplu (salvat pe Google Drive):**

```python
# Clone repo & set working dir
!git clone https://github.com/pasatsanduadrian/calendar-heatmap-dash.git
%cd calendar-heatmap-dash

# Install dependencies
!pip install -r requirements.txt

# (Opțional) Montează Google Drive și copiază fișierul Excel în folder
from google.colab import drive
drive.mount('/content/drive')
!cp /content/drive/MyDrive/Colab\ Notebooks/cal.xlsx ./

# Creează .env cu token și hostname
with open(".env", "w") as f:
    f.write("NGROK_TOKEN=tokenul_tău_ngrok_aici\n")
    f.write("NGROK_HOSTNAME=stable-guided-buck.ngrok-free.app\n")
    f.write("EXCEL_PATH=cal.xlsx\n")

# Rulează aplicația
!python app.py
```
**Ai nevoie de:**
- Un token ngrok ([îl poți genera aici](https://dashboard.ngrok.com/get-started/your-authtoken))
- (opțional) Un hostname static rezervat în dashboardul ngrok (dacă vrei link fix)

---

## 📝 Format fișier Excel (minim) și exemplu de test

| dtstart            |
|--------------------|
| 2015-09-11 11:00:00|
| 2015-09-18 09:00:00|
| ...                |

- **Foaia trebuie să se numească `Sheet1`** (sau modifică parametrul în `.env` sau direct în cod).
- Pentru testare rapidă poți descărca un exemplu:  
  👉 [**Descarcă fișierul cal.xlsx de aici (Google Sheets)**](https://docs.google.com/spreadsheets/d/1-iFenFTsSyQwU-OybhLKwjmVNbdsbjNM/edit?usp=sharing&ouid=110223860124363980416&rtpof=true&sd=true)  
    - După accesare: **File → Download → Microsoft Excel (.xlsx)**
