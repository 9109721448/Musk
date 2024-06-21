import streamlit as st
import pandas as pd
import plotly.exceptions as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *

st.set_page_config(page_title="Dashboard",page_icon="House",layout="wide")
st.subheader("Muskan Enterprises")
st.markdown("##")

def view_all_data:
result = view_all_data()
df=pd.DataFrame(result,columns=["Cement","Steel","Solution"])

st.sidebar.image("data/logo.png", caption="Build Nice")

