import streamlit as st

st.title("Simple Gender Classification")
st.subheader("Let's classify gender!")


btn_click = st.button("Click here to know more... :point_left:")

if btn_click == True:
    st.write("It represents the education level as per gender. Gender equality is a global priority at UNESCO. While much progress has been made, large gender gaps still exist in education in many settings, most often at the expense of girls, although in some regions boys are at a disadvantage. Globally, 118.5 million girls and 125.5 million boys are out of school. Women still account for almost two-thirds of all adults unable to read.")
    