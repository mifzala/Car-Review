import streamlit as st

car_info = [{
    "Brand": "Lamborghini",
    "Model": "Gallardo",
    "Born": "2003",
    "Price": "$130.000"
}, {
    "Brand": "Lamborghini",
    "Model": "Aventador",
    "Born": "2011",
    "Price": "$500.000"
}, {
    "Brand": "Lamborghini",
    "Model": "Revuelto",
    "Born": "2023",
    "Price": "$750.000"
}, {
    "Brand": "Koenigsegg",
    "Model": "Agera",
    "Born": "2011",
    "Price": "$1.500.000"
}, {
    "Brand": "Koenigsegg",
    "Model": "Gemera",
    "Born": "2020",
    "Price": "$2.000.000"
}, {
    "Brand": "Koenigsegg",
    "Model": "Jesko Absolut",
    "Born": "2019",
    "Price": "$3.200.000"
}, {
    "Brand": "Bugatti",
    "Model": "Chiron Sport",
    "Born": "2016",
    "Price": "$3.200.000"
}, {
    "Brand": "Bugatti",
    "Model": "Bolide",
    "Born": "2020",
    "Price": "$4.700.000"
}, {
    "Brand": "Bugatti",
    "Model": "Centodieci",
    "Born": "2019",
    "Price": "$9.000.000"
}]

st.markdown('# Welcome to my showroom')
st.markdown('### Which car would you like to see?')

option = st.selectbox('Choose your car', [
    car_info[0]['Brand'] + " " + car_info[0]['Model'],
    car_info[1]['Brand'] + " " + car_info[1]['Model'],
    car_info[2]['Brand'] + " " + car_info[2]['Model'],
    car_info[3]['Brand'] + " " + car_info[3]['Model'],
    car_info[4]['Brand'] + " " + car_info[4]['Model'],
    car_info[5]['Brand'] + " " + car_info[5]['Model'],
    car_info[6]['Brand'] + " " + car_info[6]['Model'],
    car_info[7]['Brand'] + " " + car_info[7]['Model'],
    car_info[8]['Brand'] + " " + car_info[8]['Model'],
])

if option == car_info[0]['Brand'] + " " + car_info[0]['Model']:
    st.image('Lamborghini.Gallardo.jpg' , width= 600,
             caption = "Release: " + str(car_info[0]['Born']) + " " + \
                "Price: " + str(car_info[0]['Price']))
    
if option ==  car_info[1]['Brand'] + " " + car_info[1]['Model']:
    st.image('Lamborghini Aventador.jpg', width= 500,
             caption = "Release: " + str(car_info[1]['Born']) + " " + \
                "Price: " + str(car_info[1]['Price']))
    
if option == car_info[2]['Brand'] + " " + car_info[2]['Model']:
    st.image('Lamborghini Revuelto.jpg', width= 600,
             caption = "Release: " + str(car_info[2]['Born']) + " " + \
                 "Price: " + str(car_info[2]['Price']))
    
if option == car_info[3]['Brand'] + " " + car_info[3]['Model']:
    st.image('Koenigsegg Agera.jpg', width= 600,
             caption = "Release: " + str(car_info[3]['Born']) + " " + \
                 "Price: " + str(car_info[3]['Price']))
    
if option == car_info[4]['Brand'] + " " + car_info[4]['Model']:
    st.image('Koenigsegg Gemera.jpg', width= 600,
             caption = "Release: " + str(car_info[4]['Born']) + " " + \
                 "Price: " + str(car_info[4]['Price']))
    
if option == car_info[5]['Brand'] + " " + car_info[5]['Model']:
    st.image('Koenigsegg Jesko Absolut.jpg', width= 600,
             caption = "Release: " + str(car_info[5]['Born']) + " " + \
                 "Price: " + str(car_info[5]['Price']))
    
if option == car_info[6]['Brand'] + " " + car_info[6]['Model']:
    st.image('Bugatti Chiron.jpg', width= 600,
             caption = "Release: " + str(car_info[6]['Born']) + " " + \
                 "Price: " + str(car_info[6]['Price']))

if option == car_info[7]['Brand'] + " " + car_info[7]['Model']:
    st.image('Bugatti Bolide.avif', width= 600,
             caption = "Release: " + str(car_info[7]['Born']) + " " + \
                "Price: " + str(car_info[7]['Price']))
    
if option == car_info[8]['Brand'] + " " + car_info[8]['Model']:
    st.image('Bugatti Centodieci.jpg', width= 600,
             caption = "Release: " + str(car_info[8]['Born']) + " " + \
                "Price: " + str(car_info[8]['Price']))




