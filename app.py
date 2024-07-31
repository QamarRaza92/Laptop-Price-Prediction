from flask import Flask,url_for,redirect,render_template,flash,request
from form import InputForm
import pickle
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
pipe = pickle.load(open('laptop.pkl','rb'))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/predict',methods=['GET','POST'])
def predict():
    message = ''
    form = InputForm()
    if form.validate_on_submit():
        Company = form.Company.data
        TypeName = form.TypeName.data
        Inches = form.Inches.data
        ScreenResolution = form.ScreenResolution.data
        OpSys = form.OpSys.data
        CPU_company = form.CPU_company.data
        Processor_gen = form.Processor_gen.data
        RAM = form.RAM.data
        ROM = form.ROM.data
        ROM_byte = form.ROM_Byte.data
        Storage_Drive = form.Storage_Drive.data
        df = pd.DataFrame({'Company':[Company],
                           'TypeName':[TypeName],
                           'Inches':[Inches],
                           'ScreenResolution':[ScreenResolution],
                           'OpSys':[OpSys],
                           'CPU Company':[CPU_company],
                           'Processor Generation/Series':[Processor_gen],
                           'RAM in GB':[RAM],
                           'ROM':[ROM],
                           'ROM Byte':[ROM_byte],
                           'Storage_Drive':[Storage_Drive]})
        price = int(pipe.predict(df))
        message = f"The Predicted Price is : {price}"
    return render_template('predict.html',form=form,output=message,title='Prediction')

if __name__ == "__main__":
    app.run(debug=True)
