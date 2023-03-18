import streamlit as st
st.title("BMI Calculator")

name= st.text_input("Name")
st.radio("Select Gender",('Male','Female'))
age=st.number_input('Enter Your Age:')
address=st.text_input("Address")
st.write('Hobbies')
hobbbies1=st.checkbox("Drawing")
hobbbies2=st.checkbox("Singing")
hobbbies3=st.checkbox("Travel")
hobbbies4=st.checkbox("Photography")
weight=st.number_input('Enter Your Weight:')
hei=st.number_input('Enter Your height:')
height=hei*0.01
bmi = weight/float(height*height)
st.write('Your BMI value is:',bmi,"kg/m2")
x=weight/float(height**2)
if x<18.5:
    st.write("Underwheight")
if x>=18.5 and x<25:
    st.image("normal.png")
    ans="       You are in Healthy weight Range"
    if x>= 25 and x< 30:
        st.image("overweight.png")
        ans="      you are in Overweight Range"
        if x>=30:
            st.image("obesity.png")
            ans="You are in Obesity Range"
st.write(ans)