from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('used_car_price_pred.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    Fuel_Type_Electric=0
    Fuel_Type_LPG=0
    Fuel_Type_Petrol=0
    Fuel_Type_CNG=0
    Brand_Name_Audi=0
    Brand_Name_BMW = 0
    Brand_Name_Bentley = 0
    Brand_Name_Chevrolet = 0
    Brand_Name_Datsun = 0
    Brand_Name_Fiat = 0
    Brand_Name_Force = 0
    Brand_Name_Ford = 0
    Brand_Name_Honda = 0
    Brand_Name_Hyundai = 0
    Brand_Name_Isuzu = 0
    Brand_Name_Jaguar = 0
    Brand_Name_Jeep = 0
    Brand_Name_Lamborghini = 0
    Brand_Name_Land = 0
    Brand_Name_Mahindra = 0
    Brand_Name_Maruti = 0
    Brand_Name_Mercedes = 0
    Brand_Name_Mini = 0
    Brand_Name_Mitsubishi = 0
    Brand_Name_Nissan = 0
    Brand_Name_Porsche = 0
    Brand_Name_Renault = 0
    Brand_Name_Skoda = 0
    Brand_Name_Smart = 0
    Brand_Name_Tata = 0
    Brand_Name_Toyota = 0
    Brand_Name_Volkswagen = 0
    Brand_Name_Volvo = 0
    Region_North=0
    Region_South=0
    Region_West=0
    Region_East=0
    if request.method == 'POST':
        Year=int(request.form['Year'])
        Mileage=float(request.form['Mileage'])
        Engine=float(request.form['Engine'])
        Power=float(request.form['Power'])
        Seats= int(request.form['Seats'])
        Kilometers_Driven=float(request.form['Kms_Driven'])
        Owner_Type=request.form['Owner_Type']
        Brand_Name = request.form['Brand_Name']
        Fuel_Type=request.form['Fuel_Type_Petrol']
        Region = request.form['Region']
        if(Fuel_Type=='Petrol'):
            Fuel_Type_Petrol=1
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Diesel=1
        elif(Fuel_Type=='Electric'):
            Fuel_Type_Electric=1
        elif(Fuel_Type=='LPG'):
            Fuel_Type_LPG=1
        else:
            Fuel_Type_CNG=1
        if (Owner_Type == 'First'):
            Owner_Type = 4
        elif (Owner_Type == 'Second'):
            Owner_Type = 3
        elif (Owner_Type == 'Third'):
            Owner_Type = 2
        else:
            Owner_Type = 1
        if (Brand_Name == 'Audi'):
            Brand_Name_Audi = 1
        elif (Brand_Name == 'BMW'):
            Brand_Name_BMW = 1
        elif (Brand_Name == 'Bentley'):
            Brand_Name_Bentley = 1
        elif (Brand_Name == 'Chevrolet'):
            Brand_Name_Chevrolet = 1
        elif (Brand_Name == 'Datsun'):
            Brand_Name_Datsun = 1
        elif (Brand_Name == 'Fiat'):
            Brand_Name_Fiat = 1
        elif (Brand_Name == 'Force'):
            Brand_Name_Force = 1
        elif (Brand_Name == 'Ford'):
            Brand_Name_Ford = 1
        elif (Brand_Name == 'Honda'):
            Brand_Name_Honda = 1
        elif (Brand_Name == 'Hyundai'):
            Brand_Name_Hyundai = 1
        elif (Brand_Name == 'Isuzu'):
            Brand_Name_Isuzu = 1
        elif (Brand_Name == 'Jaguar'):
            Brand_Name_Jaguar = 1
        elif (Brand_Name == 'Jeep'):
            Brand_Name_Jeep = 1
        elif (Brand_Name == 'Lamborghini'):
            Brand_Name_Lamborghini = 1
        elif (Brand_Name == 'Land'):
            Brand_Name_Land = 1
        elif (Brand_Name == 'Mahindra'):
            Brand_Name_Mahindra = 1
        elif (Brand_Name == 'Maruti'):
            Brand_Name_Maruti = 1
        elif (Brand_Name == 'Mercedes-Benz'):
            Brand_Name_Mercedes = 1
        elif (Brand_Name == 'Mini'):
            Brand_Name_Mini = 1
        elif (Brand_Name == 'Mitsubishi'):
            Brand_Name_Mitsubishi = 1
        elif (Brand_Name == 'Nissan'):
            Brand_Name_Nissan = 1
        elif (Brand_Name == 'Porsche'):
            Brand_Name_Porsche = 1
        elif (Brand_Name == 'Renault'):
            Brand_Name_Renault = 1
        elif (Brand_Name == 'Skoda'):
            Brand_Name_Skoda = 1
        elif (Brand_Name == 'Smart'):
            Brand_Name_Smart = 1
        elif (Brand_Name == 'Tata'):
            Brand_Name_Tata = 1
        elif (Brand_Name == 'Toyota'):
            Brand_Name_Toyota = 1
        elif (Brand_Name == 'Volkswagen'):
            Brand_Name_Volkswagen = 1
        elif (Brand_Name == 'Volvo'):
            Brand_Name_Volvo = 1
        else:
            Brand_Name_Tata=0
        if (Region == 'North'):
            Region_North = 1
        elif (Region == 'South'):
            Region_South = 1
        elif (Region == 'West'):
            Region_West = 1
        else:
            Region_East = 1
        no_year=2021-Year
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Kilometers_Driven,Owner_Type,Mileage,Engine,Power,Seats,no_year,Fuel_Type_Diesel,Fuel_Type_Electric,Fuel_Type_LPG,Fuel_Type_Petrol,Transmission_Mannual,Brand_Name_Audi,Brand_Name_BMW,Brand_Name_Bentley,Brand_Name_Chevrolet,Brand_Name_Datsun,Brand_Name_Fiat,Brand_Name_Force,Brand_Name_Ford,Brand_Name_Honda,Brand_Name_Hyundai,Brand_Name_Isuzu,Brand_Name_Jaguar,Brand_Name_Jeep,Brand_Name_Lamborghini,Brand_Name_Land,Brand_Name_Mahindra,Brand_Name_Maruti,Brand_Name_Mercedes,Brand_Name_Mini,Brand_Name_Mitsubishi,Brand_Name_Nissan,Brand_Name_Porsche,Brand_Name_Renault,Brand_Name_Skoda,Brand_Name_Smart,Brand_Name_Tata,Brand_Name_Toyota,Brand_Name_Volkswagen,Brand_Name_Volvo,Region_North,Region_South,Region_West]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)

