import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


st.subheader('Daromad xavfini prognoz qilish tizimi')

model_selected = st.radio('Qanday tahlildan foydalanmoqchisiz?', ('LogisticRegression','RandomForestClassifier','CatBoostClassifier', 'AdaBoostClassifier', 'Default'))

if model_selected == 'LogisticRegression':
    pickle_in = open("risk_of_plant_LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['RandomForestClassifier', 'Default']:
    pickle_in = open("risk_of_plant_RandomForest.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'CatBoostClassifier':
    pickle_in = open("risk_of_plant_Catboost.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'AdaBoostClassifier':
    pickle_in = open("risk_of_plant_Adaboost.pkl","rb")
    classifier=pickle.load(pickle_in)
    
    
    
    def predict_note_authentication(type, Органические_вещества, Содержание_соли,
       Климатические_условия, Уровень_возвышенности_над_уровнем_моря,
       Температура):
    prediction=classifier.predict([[type, Органические_вещества, Содержание_соли,
       Климатические_условия, Уровень_возвышенности_над_уровнем_моря,
       Температура]])
    print(prediction)
    return prediction




def main():
    st.title("Daromad xavfini prognoz qilish tizimi")
    type = st.radio('sizda qanday o simlik bor?(0 - sabzi , 1 - kartoshka)', (0, 1))
    Органические_вещества = st.number_input('sizning organik moddalar indeksingiz qanday?(faqat raqamlarni kiriting 0.5 - 5.0)', step=1, value=0)
    Содержание_соли = st.number_input('sizning tuzingiz qanday?(faqat raqamlarni kiriting 0.0 - 2.0)', step=1, value=0) 
     Климатические_условия = st.radio('sizning iqlim sharoitingiz qanday?(0 - тропический , 1 - субтропический, 2 - северный)', (0, 1, 2))
    Уровень_возвышенности_над_уровнем_моря = st.number_input('dengiz sathidagi balandligingiz?(faqat raqamlarni kiriting 1000 - 8000)', step=1, value=0)
    Температура = st.number_input('harorat ko rsatkichi)(faqat raqamlarni kiriting 15-35)', step=1, value=0)
    
    
    
    
    result=""
    if st.button("Bashorat qilish"):
        result=int(predict_note_authentication(type, Органические_вещества, Содержание_соли,
       Климатические_условия, Уровень_возвышенности_над_уровнем_моря,
       Температура)) 
     #st.success('The output is {}'.format(result))
        if result ==0:
            st.success('Ajoyib yangilik, siz bu hosilni ekishingiz mumkin')
        else:
            st.success('Yomon xabar, siz siz bu hosilni ekolmaysiz')
    
    if __name__ == '__main__':
    main()
            
    
    