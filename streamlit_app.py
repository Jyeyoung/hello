
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)
st.title("this is the app title")
st.header("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

st.checkbox('yes')
st.button('Click')
st.radio('Pick your agender',['Male','Fmale'])
st.selectbox('choose a planer',['Jupiter','Mars','neptune'])
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('Pick a number',0,50)
         