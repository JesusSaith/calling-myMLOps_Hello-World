import json
import streamlit as st
import requests

SERVER_URL = 'https://linear-model-service-jesussaith.cloud.okteto.net/v1/models/linear-model:predict'  # Actualiza con tu dirección local

def make_prediction(inputs):
    
    predict_request = {'instances': [inputs]}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

def main():
    st.title('Estimador de Predicciones de Ventas')

    # Interfaz de usuario para ingresar el gasto en publicidad
    gasto_publicidad = st.number_input('Gasto en Publicidad (x):', min_value=0.0, step=1.0)

    if st.button('Predecir'):
        prediction = make_prediction(gasto_publicidad)
        st.write(f'La predicción de ventas para un gasto en publicidad de {gasto_publicidad} es: {prediction["predictions"][0]:.2f}')


if __name__ == '__main__':
    main()
