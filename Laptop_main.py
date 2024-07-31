import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
df = pd.read_csv("C:\\Users\\moham\\Downloads\\laptop_price.csv",encoding='latin1')



df.drop(columns=['laptop_ID','Weight','Product'],axis=1,inplace=True)   



#Removing company with less than 10 laptops
df = df[(df['Company'] == 'Dell') | (df['Company'] == 'Lenovo') | (df['Company'] == 'HP') | (df['Company'] == 'Asus') | (df['Company'] == 'Acer') | (df['Company'] == 'MSI') | (df['Company'] == 'Toshiba') | (df['Company'] == 'Apple')]
df['Company'].value_counts()



#Removing "ScreenResolution", 'values_counts' of which is less than 10
df = df[(df['ScreenResolution'] == 'Full HD 1920x1080') | (df['ScreenResolution'] == '1366x768') | (df['ScreenResolution'] == 'IPS Panel Full HD 1920x1080') | (df['ScreenResolution'] == 'IPS Panel Full HD / Touchscreen 1920x1080') | (df['ScreenResolution'] == 'Full HD / Touchscreen 1920x1080') | (df['ScreenResolution'] == '1600x900') | (df['ScreenResolution'] == 'Touchscreen 1366x768') | (df['ScreenResolution'] == 'Quad HD+ / Touchscreen 3200x1800') | (df['ScreenResolution'] == 'IPS Panel 4K Ultra HD 3840x2160') | (df['ScreenResolution'] == 'IPS Panel 4K Ultra HD / Touchscreen 3840x2160')]



df['Cpu'].value_counts()
df['CPU Company'] = df['Cpu'].str.split(' ').str[0]



def generation(value):
    if 'Intel' in value:
        return value.split(' ')[2]
    else:
        return value.split(' ')[1]
    


df['Processor Generation/Series'] = df['Cpu'].apply(generation)



def converter(arg):
    import re
    pattern = r'\d+'
    return int(re.findall(pattern, arg)[0])



df['RAM in GB'] = df['Ram'].apply(converter)
df['RAM in GB'].value_counts()



df['ROM'] = df['Memory'].apply(converter)
df['ROM'].value_counts()



def storage_drive(arg):
    if 'SSD' in arg:return 'SSD'
    elif 'HDD' in arg:return 'HDD'
    else:return 'Flash Storage'



df['Storage_Drive'] = df['Memory'].apply(storage_drive)
df['Storage_Drive'].value_counts()



def Byte(arg):
    if 'GB' in arg:return 'GB'
    elif 'TB' in arg:return 'TB'



df['Byte'] = df['Memory'].apply(Byte)
df['Byte'].value_counts()



#Changing "Price_euros" column values from euros to rupees
df['Price in Rupees'] = df['Price_euros'].apply(lambda x:x*90.62)



df.drop(columns=['Cpu','Ram','Memory','Gpu','Price_euros'],axis=1,inplace=True)



df.rename(columns={'Byte':'ROM Byte'},inplace=True)



df = df[df['OpSys']!='Windows 10 S']



df = df[df['OpSys']!='Mac OS X']



#Importing all necessary libraries first
from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import MinMaxScaler,OneHotEncoder
from sklearn.pipeline        import Pipeline
from sklearn.compose         import ColumnTransformer
from sklearn.decomposition   import PCA
from sklearn.metrics         import r2_score,accuracy_score
from sklearn.linear_model    import LinearRegression
from sklearn.tree            import DecisionTreeRegressor
from sklearn.ensemble        import RandomForestRegressor,AdaBoostRegressor,VotingRegressor,BaggingRegressor



X_train,X_test,y_train,y_test = train_test_split(df.drop(columns=['Price in Rupees'],axis=1),df['Price in Rupees'],random_state=0,test_size=0.2)
print(f"X_train shape : {X_train.shape}\nX_test shape : {X_test.shape}\ny_train shape : {y_train.shape}\ny_test shape : {y_test.shape}")



transformer = ColumnTransformer(
                                [
                                    ('OneHotEncoding',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'),['Company','TypeName','ScreenResolution','OpSys','CPU Company','Processor Generation/Series','Storage_Drive','ROM Byte']),  
                                    ('MinMaxScaling',MinMaxScaler(),['Inches'])    
                                ],
                                remainder='passthrough'
                                )



pipe = Pipeline(steps=[('transforming',transformer),('Training',RandomForestRegressor())])



import warnings
warnings.filterwarnings('ignore')
pipe.fit(X_train,y_train)
ypred = pipe.predict(X_test)
print('accuracy score is : ',int(r2_score(ypred,y_test)*100),'%')



import pickle
pickle.dump(pipe,open('laptop.pkl','wb'))
