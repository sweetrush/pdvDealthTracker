import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import duckdb






# Configuring the APP
st.set_page_config(page_title="NC Death Reportor", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# --- Streamlit App Configuration ---
with st.sidebar:
    st.title("New Caledonia Death Reporter")

    # --- File Uploader ---

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is None:
        st.info("Please Upload a file", icon="I")
        st.stop()


    year = st.selectbox("Year", 
                 [
                   "2011",
                   "2012",
                   "2013",
                   "2014",
                   "2014",
                   "2015",
                   "2016",
                   "2017",
                   "2018",
                   "2019",
                   "2020",
                   "2021",
                   "2022",
                   "2023",
                 ], index=0)

# --- Data Processing and Visualization ---
if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)
        
        with st.expander("NC Death Data", expanded=False):
            df = duckdb.sql(f"""
                SELECT "Death Year","Sex"
                FROM df
                WHERE "Death Year"="""+year+"""
                """).df()

            st.dataframe(df )
    


    except Exception as e:
        st.error(f"An error occurred: {e}") 