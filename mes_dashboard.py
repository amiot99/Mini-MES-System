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

columns_to_show = [
    "order_id", "model", "maker", "product_id",
    "quantity", "due_date", "status", "origin",
    "created_at", "log_timestamp"
]

selected_statuses = st.multiselect("Filter by Status", filtered_df["status"].unique())

if selected_statuses:
    filtered_df = filtered_df[filtered_df["status"].isin(selected_statuses)]


st.subheader("All Logged Orders")
st.dataframe(filtered_df[columns_to_show])

# Show order status counts as a bar chart
st.subheader("Order Status Breakdown")
status_counts = filtered_df["status"].value_counts()
st.bar_chart(status_counts)