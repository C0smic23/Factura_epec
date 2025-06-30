import streamlit as st

def calcular_factura(consumo1, consumo2):
    consumo_total_kwh = 480
    total_facturado = 110233.60
    neto_epec = 77964.04
    impuestos_y_tasas = total_facturado - neto_epec

    if abs((consumo1 + consumo2) - consumo_total_kwh) > 1:
        return None, None, None

    prop1 = consumo1 / consumo_total_kwh
    prop2 = consumo2 / consumo_total_kwh

    pago1 = neto_epec * prop1 + (impuestos_y_tasas / 2)
    pago2 = neto_epec * prop2 + (impuestos_y_tasas / 2)

    return total_facturado, pago1, pago2

st.title("💡 Cálculo de factura EPEC compartida")

consumo1 = st.number_input("Consumo de persona 1 (kWh)", min_value=0.0, step=1.0)
consumo2 = st.number_input("Consumo de persona 2 (kWh)", min_value=0.0, step=1.0)

if st.button("Calcular"):
    total, pago1, pago2 = calcular_factura(consumo1, consumo2)
    if total:
        st.success(f"Total facturado: ${total:,.2f}")
        st.write(f"👤 Persona 1 debe pagar: ${pago1:,.2f}")
        st.write(f"👤 Persona 2 debe pagar: ${pago2:,.2f}")
    else:
        st.error("⚠️ La suma de consumos no coincide con el total de 480 kWh")
