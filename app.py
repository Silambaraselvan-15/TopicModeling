import streamlit as st
import pandas as pd

# Load the CSV file
articleDataFrame = pd.read_csv("indian_express_articles.csv")

# Streamlit app
st.title("Indian Express Article Topic Finder")

searchInput = st.text_input("Enter a headline or description to search:")

if searchInput:
    # Search for matching rows in 'headlines' or 'description' columns
    searchMask = articleDataFrame['headlines'].fillna('').str.contains(searchInput, case=False, na=False) | \
                 articleDataFrame['description'].fillna('').str.contains(searchInput, case=False, na=False)

    searchResults = articleDataFrame[searchMask]

    if not searchResults.empty:
        st.success(f"Found {len(searchResults)} matching articles:")
        for _, row in searchResults.iterrows():
            st.markdown(f"### {row['headlines']}")
            st.markdown(f"**Description:** {row['description']}")
            st.markdown(f"**Category:** {row['category']}")
            st.markdown("---")
    else:
        st.warning("No matching articles found.")
