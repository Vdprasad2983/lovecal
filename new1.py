import streamlit as st
import pandas as pd
import datetime
import psycopg2
import os
from pytz import timezone

# PostgreSQL connection parameters (replace with your Render PostgreSQL details)
DB_HOST = os.getenv('DB_HOST', 'dpg-crifrl68ii6s73f32mq0-a')
DB_NAME = os.getenv('DB_NAME', 'mydatabase_0xnp')
DB_USER = os.getenv('DB_USER', 'mydatabase_0xnp_user')
DB_PASS = os.getenv('DB_PASS', 'B2eixQVp1J1KSPz6qZZ6Tlb1mx3YJJ2f')
DB_PORT = os.getenv('DB_PORT', '5432')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)
cur = conn.cursor()


st.balloons()
st.header("welcome to the world of love calculator")
b1=st.text_input("enter you name",max_chars=15)
b2=st.text_input("enter your loved ones name",max_chars=15)
s=st.button("submit")
date = datetime.datetime.now(timezone("Asia/Kolkata"))

if s:
    if not b1 or not b2:
        st.warning("Please enter the mandatory fields")
        st.stop()
    c=b1+b2
    c.lower()
    t=c.count('t')
    r=c.count('r')
    u=c.count('u')
    e=c.count('e')

    l=c.count('l')
    o=c.count('o')
    v=c.count('v')
    e=c.count('e')
    love=l+o+v+e
    true=t+r+u+e
    score=int(str(true)+str(love))
    if score>80:
        st.write(f"your score is {score} you both will be great together")
    elif score >=30 and score<=80:
        st.write(f"your score is {score} and you are alright together")
    else:
        st.write(f"your love score is {score}, better to check with different name")
    
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS lovecal(
            NAME1 VARCHAR(100), NAME2 VARCHAR(100), SCORE VARCHAR(50), DATE VARCHAR(50)
        )
        """
    )
    cur.execute("INSERT INTO lovecal (NAME1, NAME2, SCORE, DATE) VALUES (%s, %s, %s, %s)",(b1, b2, str(score), date))
    conn.commit()


conn.close()
