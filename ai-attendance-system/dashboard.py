import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Attendance System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Attendance Dashboard")

DB_PATH = "database/attendance.db"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query(
    "SELECT * FROM attendance ORDER BY id DESC",
    conn
)

conn.close()

from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

today_df = df[df["date"] == today]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "👨‍🎓 Total Records",
        len(df)
    )

with col2:
    st.metric(
        "✅ Present Today",
        len(today_df)
    )

search = st.text_input("🔍 Search Student")

if search:
    df = df[
        df["name"].str.contains(
            search,
            case=False
        )
    ]

selected_date = st.date_input("📅 Select Date")

filtered = df[
    df["date"] == str(selected_date)
]

if len(filtered):

    st.dataframe(filtered)

else:

    st.info("No attendance found.")

chart = (
    df.groupby("date")
    .size()
    .reset_index(name="Attendance")
)

fig = px.bar(
    chart,
    x="date",
    y="Attendance",
    title="Daily Attendance"
)

st.plotly_chart(
    fig,
    width="stretch"
)
st.divider()

st.subheader("Attendance Records")

st.dataframe(
    df,
    width="stretch"
)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Attendance CSV",
    csv,
    "attendance.csv",
    "text/csv"
)
