import pandas as pd
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('automobile.csv')


st.markdown("<h1 style = 'color: #DD5746; text-align: center; font-size: 60px; font-family: Monospace'>AUTOMOBILE PRICE PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FFC470; text-align: center; font-family: Serif '>Built by Era King</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)

#get an image
st.image('pngwing.com (5).png', caption = 'Built by Era King')    

#Add Project problem statement
st.markdown("<h2 style = 'color: #F7C566; text-align: center; font-family: montserrat '>Background Of Study</h2>", unsafe_allow_html = True)

st.markdown("The study on automobile price prediction aims to leverage machine learning algorithms to forecast the prices of vehicles based on various features such as brand, model, mileage, year of manufacture, and additional specifications. By analyzing historical pricing data and incorporating factors like market trends, economic indicators, and consumer preferences, the research seeks to develop a predictive model that can assist buyers, sellers, and industry professionals in making informed decisions. This study not only contributes to enhancing pricing strategies in the automotive market but also provides valuable insights into the factors influencing vehicle prices in a dynamic and competitive industry.</p>", unsafe_allow_html=True)

# Sidebar design (to put what you want on the side)
st.sidebar.image('pngwing.com (6).png')

# markdown is for space
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.header('Project Data')
st.dataframe(data, use_container_width= True)

# user inputs
curb_weight = st.sidebar.number_input("curb-weight", placeholder='insert your numbers...')
symboling = st.sidebar.number_input('symboling', placeholder='insert a number...')
normalized_losses = st.sidebar.number_input ('normalized-losses', data ['normalized-losses'].min(), data['normalized-losses'].max())
make = st.sidebar.selectbox ('make', data['make'].unique())
body_style = st.sidebar.selectbox ('body-style', data['body-style'].unique())
horsepower = st.sidebar.number_input ("horsepower", placeholder='insert your numbers...')
height = st.sidebar.number_input("height", placeholder='insert your numbers...')




# user input dataframe
user_input = pd.DataFrame()
user_input['curb-weight'] = [curb_weight]
user_input['symboling'] = [symboling]
user_input['normalized-losses'] = [normalized_losses]
user_input['make'] = [make]
user_input['horsepower'] = [horsepower]
user_input['height'] = [height]
user_input['body-style'] = [body_style]

st.markdown("<b>", unsafe_allow_html = True)
st.header('input Variable')
st.dataframe(user_input, use_container_width = True)


# import transformers
make = joblib.load('make_encoder.pkl')
body_style = joblib.load('body-style_encoder.pkl')


# tarnsform user input according to training scale and encoding
user_input['make'] = make.transform(user_input[['make']])
user_input['body-style'] = body_style.transform(user_input[['body-style']])

st.dataframe(user_input)
model = joblib.load('autoMobilePredmodel.pkl')

if st.button('Price Profitability'):
    predicted_price = model.predict(user_input)
    st.success(f"Your predicted profit is {predicted_price[0].round()}")
    st.snow()




