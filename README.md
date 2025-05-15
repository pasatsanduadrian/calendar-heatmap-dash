# 📅 Calendar Heatmap Dash App

Aplicație Dash/Python pentru generarea și vizualizarea unui heatmap calendaristic interactiv (stil GitHub), pe baza datelor dintr-un fișier Excel cu evenimente zilnice.

---

## ⚡️ Funcționalități

- Selectare rapidă a anului (dropdown).
- Heatmap interactiv cu hover/tooltip pe fiecare zi (plotly).
- Pagina web accesibilă public via ngrok (link static sau dinamic).
- Configurare ușoară pentru propriul tău fișier Excel.

---

## 📦 Instalare rapidă

1. **Clonează proiectul:**
    ```bash
    git clone https://github.com/<user>/calendar-heatmap-dash.git
    cd calendar-heatmap-dash
    ```

2. **Instalează dependențele:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Adaugă fișierul tău Excel** (implicit `cal.xlsx`) în folderul proiectului.
   - Structură minimă: o coloană cu numele `dtstart` (format dată/oră, ex: 2015-09-18 09:00:00).

4. **Configurează variabilele sensibile:**
    - Creează un fișier `.env` pe baza `.env.example`.
    - Obține un token gratuit ngrok de aici: https://dashboard.ngrok.com/get-started/your-authtoken
    - (opțional) Rezervă-ți un hostname static din dashboardul ngrok (plan free/domeniu `.ngrok-free.app`).

5. **Pornește aplicația:**
    ```bash
    python app.py
    ```

6. **Accesează linkul generat** de ngrok din terminal (de exemplu `https://hostnameul-tau.ngrok-free.app`).

---

## 📝 Format fișier Excel (minim)

| dtstart            |
|--------------------|
| 2015-09-11 11:00:00|
| 2015-09-18 09:00:00|
| ...                |

- Foaia trebuie să se numească `Sheet1` (sau modifică parametrul în `.env` sau direct în cod).

---

## ⚠️ Securitate
- **Nu publica tokenul tău NGROK în repo public!** (e motivul pentru care există `.env.example` și `.gitignore`)
- Recomandăm să-ți setezi `.env` doar local.

---

## 🔧 Customizare
- Poți schimba calea fișierului Excel în `.env` sau la începutul `app.py`.
- Pentru statistici suplimentare sau grafice adiționale (bar chart/lună etc), modifică secțiunea heatmap din cod.

---

## 🤝 Contribuții
PR-urile și sugestiile sunt binevenite! Deschide un issue pentru bug-uri sau idei noi.

---

## 📄 Licență
MIT
