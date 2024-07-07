import streamlit as st

st.title('I am Title')
st.header('I am Header')
st.subheader('I am Subheader')
st.markdown('I am Markdown')
st.code('I am code block. Eg int a = 5')
st.text('I am Text')
st.write('I am Write')

var1 = 'Hello'
var2 = 5
st.write('The value of var1 = ',var1)

################################################
## DataFrame
import pandas as pd
import numpy as np
st.subheader('DataFrame')
df = pd.DataFrame({'a':np.arange(10),'b':np.arange(10)*11})
st.dataframe(df,1000,100)

###############################################
## Tables
st.subheader('Table')
st.table(df)


##############################################
## JSON
st.json(
    {
        'abc':'1',
        'xyz':'2',
        'pqr':'3'
    }
)

###############################################
###############################################

##Line chart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.line_chart(chart_data)

##Area Chart
st.area_chart(chart_data)

##bar Chart
st.bar_chart(chart_data)

##############################################
## Matplotlib functions
import matplotlib.pyplot as plt
arr = np.random.normal(1,1,size = 100)
fig,ax= plt.subplots()
ax.hist(arr,bins = 20)
st.pyplot(fig)


###############################################
###############################################

## Buttons
if st.button('Hello'):
    st.write('I am Dongle')
else:
    st.write('I am Powerbank')



## Download
sample_text = 'some random text to download'
st.download_button('Download Text',sample_text)


with open('download.jpeg','rb') as file:
    btn = st.download_button(
        label = 'Download Image',
        data = file,
        file_name = 'flower.jpeg',
        mime = 'image/jpeg'
    )

@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

df1 = pd.read_csv('^N225.csv')
csv = convert_df(df1)
st.download_button(
    label = 'Download Text',
    data = csv,
    file_name='large_text.csv',
    mime = 'text/csv'
)


## Checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Great!!!')

##radio button
genre = st.radio(
    'What is your favourite movie?',
    ('Comedy','Active','Anime')
)

if genre == 'Comedy':
    st.write('You selected the comedy movie')
else:
    st.write("you didn't select the comedy movie")


## select box
option = st.selectbox(
    'How would you like to be contacted? ',
    ('Email','Post','Gmail','Whatsapp','Facebook')
)


## Slider
from datetime import datetime
age = st.slider(
    'How old are you?',
    0,130,25
)
if age == 29:
    st.write('GilliDanda Kheloge???')
else:
    st.write('Tillu kalia')

AGE = st.slider(
    'How old are you?',
    0,130,(25,60)
)

time = st.slider(
    'How old are you?',
    datetime(2021,1,1),datetime(2024,4,1),datetime(2022,2,1)
)

##Text input
title = st.text_input('movie title','pk')
st.write('the current movie title is : ',title)



##Number input
num = st.number_input('Enter your age',25)
st.write('Your age is : ',num)

##Date input
date = st.date_input("Enter today's date",datetime(2019,7,6))
st.write("Todays's date is : ",date)


## Workung with images
from PIL import Image
image = Image.open('download.jpeg')
st.image(image,caption='landscape')


##working with vdo
vdo_file = open('vdo.mp4','rb')
vdo_bytes = vdo_file.read()
st.video(vdo_bytes)


##Side bar
st.sidebar.selectbox(
    'Choose the prefered way of contact',
    ('Email','Gmail','Whatsapp')
)

with st.sidebar:
    radio = st.radio('Choose yuor language of communication',
    ('Bengali','Hindi','English'))



## Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header('This is column 1')
    st.title('col 1')
    st.write('some text inside column 1')

with col2:
    st.header('This is column 2')
    st.title('col 2')
    st.write('some text inside column 2')

with col3:
    st.header('This is column 3')
    st.title('col 3')
    st.write('some text inside column 3')


##Expander
st.bar_chart({'data':[1,5,2,6,2,1]})

with st.expander('Expand me to see some text'):
    st.write('some text written inside expander')