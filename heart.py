# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:05:58 2021

@author: vishw
"""

import pickle
import streamlit as st



pickle_in=open('bagging.pkl','rb')
bc=pickle.load(pickle_in)

def welcome():
    return 'Welcome to heart disease prediction'

def predict_heart_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    """ We will predict here if you will get a heart disease or not.
    
    ---
    
    parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: sex
        in: query
        type: number
        required: true
      - name: cp
        in: query
        type: number
        required: true
      - name: trestbps
        in: query
        type: number
        required: true
      - name: chol
        in: query
        type: number
        required: true
      - name: fbs
        in: query
        type: number
        required: true
      - name: restecg
        in: query
        type: number
        required: true
      - name: thalach
        in: query
        type: number
        required: true
      - name: exang
        in: query
        type: number
        required: true
      - name: oldpeak
        in: query
        type: number
        required: true
      - name: slope
        in: query
        type: number
        required: true
      - name: ca
        in: query
        type: number
        required: true
      - name: thal
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
            
    """
    prediction=bc.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(prediction)
    return prediction


def main():
    st.title('Heart Disease Prediction')
    html_temp="""
    <div style="background-color:pink;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age =  st.text_input("Age")
    sex =  st.selectbox('enter gender (1 if male or 0 if female)', [0,1])
    cp =  st.selectbox("Chest Pain Type",[0,1,2,3])
    trestbps =  st.text_input("Resting BP")
    chol =  st.text_input("Serum Cholestrol in mg/dl")
    fbs =  st.text_input("Fasting Blood Sugar >120 mg/dl) (1 = true; 0 = false)")
    restecg =  st.text_input("resting ECG results")
    thalach =  st.text_input("Maximum Heart rate achieved")
    exang =  st.text_input("Exercise induced angina (1 = yes; 0 = no)")
    oldpeak =  st.text_input("ST depression induced by exercise relative to rest")
    slope =  st.text_input("Slope of peak exercise ST segment")
    ca = st.text_input("Number of major vessels (0-3) colored by flourosopy")
    thal =  st.selectbox('Select thalessemia type', [ 1, 2 ,3])
    result=''
    if st.button("Predict"):
        result=predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success('The output is {}'.format(result))
    
    
if __name__=='__main__':
    main()
     