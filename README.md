# Energie- und Kostenermittlung bei Druckerhöhung im Lüftungskanal

Dieses Projekt berechnet den Einfluss einer Erhöhung des Kanaldrucks auf den Energieverbrauch und die jährlichen Stromkosten eines Ventilators nach den **Affinitätsgesetzen**.

## ⚙️ Funktionsweise
Die Berechnung basiert auf den physikalischen Zusammenhängen:
- Volumenstrom:  V ∝ n
- Druck:         p ∝ n²
- Leistung:      P ∝ n³

Eine Druckerhöhung von 10 % führt somit zu etwa 15 % höherer Leistungsaufnahme.

## 🚀 Ausführung
### Lokal starten
1. Stelle sicher, dass **Python 3.10+** installiert ist.
2. Installiere Streamlit:
   ```bash
   pip install -r requirements.txt
