import streamlit as st
import joblib
model=joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')
ip=st.text_input('enter your message')
op=model.predict([ip])
if st.botton('Predict'):
  st.title(Op[0])
    
