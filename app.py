import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("indian_express_articles.csv")

# Streamlit app
st.title("Indian Express Article Finder")

user_input = st.text_input("Enter a headline or description to search:")

if user_input:
    # Search for matching rows in 'headlines' or 'description' columns
    mask = df['headlines'].fillna('').str.contains(user_input, case=False, na=False) | \
           df['description'].fillna('').str.contains(user_input, case=False, na=False)

    results = df[mask]

    if not results.empty:
        st.success(f"Found {len(results)} matching articles:")
        for _, row in results.iterrows():
            st.markdown(f"### {row['headlines']}")
            st.markdown(f"**Description:** {row['description']}")
            st.markdown(f"**Category:** {row['category']}")
            st.markdown("---")
    else:
        st.warning("No matching articles found.")
