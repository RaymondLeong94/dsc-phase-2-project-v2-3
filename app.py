import streamlit as st 
import pickle
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

#title
st.title("""App for Housing Price Prediction Based on *Features* """)
st.markdown("Factors: Internal, External, Geographic")

#sidebar
st.sidebar.header('Specify Input Parameters')
data = pd.read_csv("./data/Final_Data")
def user_input_features():
    sqft_living = st.sidebar.slider('sqft_living', 0, 10000, 2000)
    sqft_living15 = st.sidebar.slider('sqft_living15', 0, 10000, 2000)
    sqft_lot15_new_log = st.sidebar.slider('sqft_lot15_new_log', 0, 2, 1)
    condition_Fair = st.sidebar.slider('condition_Fair', 0, 1, 0)
    condition_Good = st.sidebar.slider('condition_Good', 0, 1, 0)
    condition_Poor = st.sidebar.slider('condition_Poor', 0, 1, 0)
    condition_Very_Good = st.sidebar.slider('condition_Very Good', 0, 1, 0)
    view_EXCELLENT = st.sidebar.slider('view_EXCELLENT', 0, 1, 0)
    view_GOOD = st.sidebar.slider('view_GOOD', 0, 1, 0)
    view_NONE = st.sidebar.slider('view_NONE', 0, 1, 0)
    waterfront_YES = st.sidebar.slider('waterfront_YES', 0, 1, 0)
    grade_11_Excellent = st.sidebar.slider('grade_11 Excellent', 0, 1, 0)
    grade_12_Luxury = st.sidebar.slider('grade_12 Luxury', 0, 1, 0)
    grade_13_Mansion = st.sidebar.slider('grade_13 Mansion', 0, 1, 0)
    grade_4_Low = st.sidebar.slider('grade_4 Low', 0, 1, 0)
    grade_5_Fair = st.sidebar.slider('grade_5 Fair', 0, 1, 0)
    grade_9_Better = st.sidebar.slider('grade_9 Better', 0, 1, 0)
    lat = st.sidebar.slider('lat', -100, 100, 50)
    long = st.sidebar.slider('long', -100, 100, 50)
    
    data = {'sqft_living' : sqft_living,
    'sqft_living15' :sqft_living15,
    'sqft_lot15_new_log' : sqft_lot15_new_log,
    'condition_Fair' : condition_Fair,
    'condition_Good': condition_Good,
    'condition_Poor' : condition_Poor,
    'condition_Very Good': condition_Very_Good,
    'view_EXCELLENT' : view_EXCELLENT,
    'view_GOOD' : view_GOOD,
    'view_NONE' : view_NONE,
    'waterfront_YES' : waterfront_YES,
    'grade_11 Excellent' : grade_11_Excellent,
    'grade_12 Luxury' : grade_12_Luxury,
    'grade_13 Mansion' : grade_13_Mansion, 
    'grade_4 Low' : grade_4_Low,
    'grade_5 Fair' : grade_5_Fair,
    'grade_9 Better' : grade_9_Better,
    'lat' : lat,
    'long' : long}


   
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

#model 
Y = data["price_log"]
X = data[["sqft_living", 
"sqft_living15", 
"sqft_lot15_new_log",
'condition_Fair',
'condition_Good',
'condition_Poor',
'condition_Very Good',
'view_EXCELLENT',
'view_GOOD',
'view_NONE',
'waterfront_YES',
'grade_11 Excellent',
'grade_12 Luxury',
'grade_13 Mansion',
'grade_4 Low',
'grade_5 Fair',
'grade_9 Better',    
 "lat", "long" ]]

#scale
sc = StandardScaler()
X = sc.fit_transform(X)

#train test split
regr = linear_model.LinearRegression().fit(X,Y)
#make y_pred = to predicting the x trained variables 
y_pred = regr.predict(df)
#model predictions based on notebook 
#model = pickle.load(open('final_model.pkl', 'rb'))
#predict

st.header('Prediction of Log(Price)')
st.write(y_pred)
st.write('---')

