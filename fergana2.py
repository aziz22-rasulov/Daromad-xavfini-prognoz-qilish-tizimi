import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

st.subheader('Выявление риска плохой урожайности')

pickle_in = open("risk_of_plant_RandomForest.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note_authentication(plant_type, Organic_matter, Salt_content,
                                Climatic_conditions, Elevation_level_above_sea_level,
                                Temperature):
    prediction = classifier.predict([[plant_type, Organic_matter, Salt_content,
                                      Climatic_conditions, Elevation_level_above_sea_level,
                                      Temperature]])
    print(prediction)
    return prediction

def main():
    st.title("'Выявление риска плохой урожайности'")
    plant_type = st.radio('Что вы хотите посадить ?(0 - sabzi , 1 - kartoshka)', (0, 1))
    Organic_matter = st.number_input('индекс органических, биологических веществ?(введите цифры от  0.5% - 5.0%)', step=0.1, value=0.0)
    Salt_content = st.number_input('индекс солесодержания?(введите данные от 0.0мСм/см - 2.0мСм/см)', step=0.1, value=0.0)
    Climatic_conditions = st.radio('климатический регион?(0 - тропический , 1 - субтропический, 2 - северный)', (0, 1, 2))
    Elevation_level_above_sea_level = st.number_input('высота над уровнем моря?(введите цифры от 1000 - 8000)', step=1, value=0)
    Temperature = st.number_input('температура)(введите цифры от 15-35)', step=1, value=0)

    result = ""
    if st.button("Предсказать"):
        result = int(predict_note_authentication(plant_type, Organic_matter, Salt_content,
                                                Climatic_conditions, Elevation_level_above_sea_level,
                                                Temperature))
        if result == 0:
            st.success('Отлично, вы можете посадить эту культуру')
        else:
            st.success('Плохие новости, вы не можете посадить данную культуру')

if __name__ == '__main__':
    main()
      