import streamlit as st
from utils import *
import pandas as pd


if __name__=="__main__":
    st.write("# Test Planner")
    subj = st.text_input("Enter Subject")
    topic = st.text_input("Enter Topic")
    addn = st.text_input("Any aditional remark")
    addEvent = st.button("Submit")
    showEvent = st.button("Show Schedule")
    if addEvent:
        updateCal(subj, topic, addn)
    if showEvent:
        df = pd.DataFrame(show(), columns=["Date", "Subject: Topic", "Remark"])
        df.index = [i+1 for i in range(len(df))]
        st.table(df)
