import pandas as pd
import streamlit as st

from finance_data_extractor import extract_data

st.title("Finance Data Extractor")
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Input Article")
    article_text = st.text_area("Paste the finance-related article here:", height=330)

    # Button to extract data
    if st.button("Extract"):
        if article_text.strip():
            financial_data = extract_data(article_text)
        else:
            st.warning("Please enter an article to extract data!")
            financial_data = pd.DataFrame()
    else:
        financial_data = pd.DataFrame()

with col2:
    st.subheader("Extracted Financial Data")
    # Define empty table initially
    initial_data = {
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Values": ["", "", "", "", ""],
    }

    # Update the table if data is extracted
    if financial_data.empty:
        financial_data = pd.DataFrame(initial_data)
    st.dataframe(
        financial_data,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Values": st.column_config.Column(width=150),
        },
        hide_index=True,
    )
