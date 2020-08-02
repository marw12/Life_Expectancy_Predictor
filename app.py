import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import flask

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():    
        return(flask.render_template('index.html'))
    


@app.route('/predict',methods=['POST'])
def predict():
        inputStatus = flask.request.form['inputStatus']
        
        if inputStatus == 'Developed':
            inputStatus = 0
        elif inputStatus == 'Developing':
            inputStatus = 1
        
        inputMortality = flask.request.form['inputMortality']
        inputInfantDeath = flask.request.form['inputInfantDeath']
        inputAlcohol = flask.request.form['inputAlcohol']
        inputHepatitis = flask.request.form['inputHepatitis']
        inputBMI = flask.request.form['inputBMI']
        inputUnder5Deaths = flask.request.form['inputUnder5Deaths']
        inputPolio = flask.request.form['inputPolio']
        inputTotalExpenditure = flask.request.form['inputTotalExpenditure']
        inputDiptheria = flask.request.form['inputDiptheria']
        inputAIDS = flask.request.form['inputAIDS']
        inputThinness19 = flask.request.form['inputThinness19']
        inputThinness9 = flask.request.form['inputThinness9']
        inputIncome = flask.request.form['inputIncome']
        inputSchooling = flask.request.form['inputSchooling']
        
        input_variables = pd.DataFrame([[inputStatus, inputMortality, inputInfantDeath, inputAlcohol, inputHepatitis, inputBMI, inputUnder5Deaths, inputPolio, inputTotalExpenditure, inputDiptheria, inputAIDS, inputThinness19, inputThinness9, inputIncome, inputSchooling]],
                                       columns=['inputStatus', 'inputMortality', 'inputInfantDeath', 'inputAlcohol', 'inputHepatitis', 'inputBMI', 'inputUnder5Deaths', 'inputPolio', 'inputTotalExpenditure', 'inputDiptheria', 'inputAIDS', 'inputThinness19', 'inputThinness9', 'inputIncome', 'inputSchooling'],
                                       dtype=float)
        
        prediction = model.predict(input_variables)[0]
        prediction = round(prediction, 1)
        
        return flask.render_template('index.html', prediction_text= '{} Years'.format(prediction))


@app.route('/about', methods=['GET'])
def about():    
        return(flask.render_template('about.html'))
        
        
@app.route('/contact', methods=['GET'])
def contact():    
        return(flask.render_template('contact.html'))


if __name__ == "__main__":
    app.run(debug=True)
    