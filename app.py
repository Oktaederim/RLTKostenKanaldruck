import streamlit as st

st.title("Energie- und Kostenermittlung bei Druckerhöhung im Lüftungskanal")
st.write("Berechnung nach den Affinitätsgesetzen der Ventilatortechnik")

# Eingaben
P1 = st.number_input("Nennleistung [kW]", value=5.0)
p1 = st.number_input("Nenndruck [Pa]", value=600.0)
n1 = st.number_input("Nenndrehzahl [1/min]", value=1450.0)
druck_anstieg = st.slider("Druckerhöhung [%]", 0.0, 50.0, 10.0)
strompreis = st.number_input("Strompreis [€/kWh]", value=0.25)
stunden_pro_tag = st.number_input("Betriebszeit pro Tag [h]", value=10)
tage_pro_jahr = st.number_input("Betriebstage pro Jahr", value=250)

# Berechnungen
p2 = p1 * (1 + druck_anstieg / 100)
n2 = n1 * (p2 / p1) ** 0.5
P2 = P1 * (n2 / n1) ** 3

jahresenergie_alt = P1 * stunden_pro_tag * tage_pro_jahr
jahresenergie_neu = P2 * stunden_pro_tag * tage_pro_jahr
mehrverbrauch = jahresenergie_neu - jahresenergie_alt
mehrkosten = mehrverbrauch * strompreis
steigerung_leistung = (P2 / P1 - 1) * 100

# Ausgabe
st.subheader("Ergebnisse")
st.write(f"Neue Drehzahl: **{n2:.0f} 1/min**")
st.write(f"Neue Leistungsaufnahme: **{P2:.2f} kW**")
st.write(f"Jahresenergie alt: {jahresenergie_alt:,.0f} kWh")
st.write(f"Jahresenergie neu: {jahresenergie_neu:,.0f} kWh")
st.write(f"Mehrverbrauch: {mehrverbrauch:,.0f} kWh/Jahr")
st.write(f"Mehrkosten: {mehrkosten:,.2f} € pro Jahr")
st.success(f"Eine Druckerhöhung von {druck_anstieg:.1f}% führt zu "
           f"einer Leistungssteigerung von {steigerung_leistung:.1f}% "
           f"und erhöht die jährlichen Stromkosten um {mehrkosten:,.2f} €.")
