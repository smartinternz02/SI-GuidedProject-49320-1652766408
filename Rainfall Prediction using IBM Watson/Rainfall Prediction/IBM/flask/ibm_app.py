import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__,template_folder='template')

scale = pickle.load(open('scale.pkl','rb'))
label = pickle.load(open('encoder.pkl','rb'))


@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page

@app.route('/predict',methods=['post','get'])# route to show the predictions in a web UI
def predict():
    #  reading the inputs given by the user
    input_feature=[x for x in request.form.values()] 
    print(input_feature)
    input_feature[0]=float(label[input_feature[0]])
    input_feature[1]=float(input_feature[1])
    input_feature[2]=float(input_feature[2])
    input_feature[3]=float(input_feature[3])
    input_feature[4]=float(label[input_feature[4]])
    input_feature[5]=float(input_feature[5])
    input_feature[6]=float(label[input_feature[6]])
    input_feature[7]=float(label[input_feature[7]])
    input_feature[8]=float(input_feature[8])
    input_feature[9]=float(input_feature[9])
    input_feature[10]=float(input_feature[10])
    input_feature[11]=float(input_feature[11])
    input_feature[12]=float(input_feature[12])
    input_feature[13]=float(input_feature[13])
    input_feature[14]=float(input_feature[14])
    input_feature[15]=float(input_feature[15])
    input_feature[16]=float(input_feature[16])
    input_feature[17]=float(input_feature[17])
    input_feature[18]=float(input_feature[18])
    input_feature[19]=float(input_feature[19])
    input_feature[20]=float(input_feature[20])
    input_feature[21]=float(label[input_feature[21]])
    print(input_feature)
    features_values=[input_feature]
    
    names = [['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 
       'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'year', 'month', 'date', 'RainToday']]
    
    ####IBM UI#########
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "kjewOInfiBzWmlGK158pyYD6ym5sAY1tpADVzk1wrJPA"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    print("mltoken",mltoken)
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": names, "values": features_values}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9f3be84d-0c5d-4e4e-8db9-8fd4fd05cd3c/predictions?version=2022-05-30', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    pred=response_scoring.json()
    prediction=pred['predictions'][0]['values'][0][0]
    if prediction == 1:
        return render_template("chance.html")
    else:
        return render_template("nochance.html")

# showing the prediction results in a UI
if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000,debug=True)    # running the app
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)