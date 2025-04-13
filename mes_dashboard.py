import streamlit as st
import sqlite3
import pandas as pd


st.title("MES Order Dashboard")

#Connect to the MES database
conn = sqlite3.connect("order_log.db")
df = pd.read_sql_query("SELECT * FROM order_logs",conn)
conn.close()

run_ids = df["run_id"].unique() #Get all unique run IDs
selected_run = st.selectbox("Select a RUN_ID", run_ids) #Add dropdown to select one
filtered_df = df[df["run_id"] == selected_run] #Filter the table based on selection

st.subheader("All Logged Orders")
st.dataframe(filtered_df)
