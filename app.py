'''
@author: Vishal Sharbidar Mukunda

'''

from crypt import methods
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger 
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def Diabetes_prediction():
    """Lets predict the Diabetes
    This is using docstrings for specification
    ---
    tags:
    - testapi
    parameters:
        - name: Pregnancies
          in: query
          type: number
          required: true
        - name: Glucose
          in: query
          type: number
          required: true
          description: Level of Glucose in Blood
        - name: BloodPressure
          in: query
          type: number
          required: true
        - name: SkinThickness
          in: query
          type: number
          required: true
        - name: Insulin
          in: query
          type: number
          required: true
        - name: BMI
          in: query
          type: number
          required: true
        - name: DiabetesPedigreeFunction
          in: query
          type: number
          required: true
        - name: Age
          in: query
          type: number 
          required: true      
    
    responses:
        200:
            description: the output values
        
    """
    Pregnancies=request.args.get('Pregnancies')  
    Glucose=request.args.get('Glucose')  
    BloodPressure=request.args.get('BloodPressure')  
    SkinThickness=request.args.get('SkinThickness')  
    Insulin=request.args.get('Insulin')  
    BMI=request.args.get('BMI')  
    DiabetesPedigreeFunction=request.args.get('DiabetesPedigreeFunction')  
    Age=request.args.get('Age')  
    prediction=classifier.predict([[Pregnancies,Glucose,BloodPressure,
                                SkinThickness,Insulin,BMI, 
                                DiabetesPedigreeFunction,Age]])
    return 'The predicted value is ' + str(prediction)


@app.route('/predict_file', methods=['POST'])
def Diabetes_prediction_file():
    """Lets predict the Diabetes
    This is using docstrings for specification
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
        200:
            description: the output values
          
    """
    df_test=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return 'The predicted value for the csv are ' + str(list(prediction))



if __name__=='__main__':
    app.run()