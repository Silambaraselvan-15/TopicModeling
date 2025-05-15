# Indian Express Article Topic Finder

This project is a **Streamlit-based web application** designed to help users search and explore articles from **The Indian Express**. The app allows users to search for articles by their headlines or descriptions and displays relevant details such as the headline, description, and category.

---

## Features

- **Search Functionality**: Search for articles by entering keywords in the headline or description.
- **Case-Insensitive Matching**: Ensures that searches are not affected by capitalization.
- **Dynamic Results**: Displays matching articles with their headline, description, and category.
- **Interactive UI**: Built using Streamlit for a seamless and responsive experience.
- **Error Handling**: Displays a warning if no matching articles are found.

---

## Requirements

To run this application, ensure you have the following installed:

- **Python 3.7+**
- **Streamlit**
- **Pandas**

---

## Installation

Follow these steps to set up and run the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/TopicModeling.git
   cd TopicModeling
   ```

## Usage
streamlit run app.py

Make sure `indian_express_articles.csv` is in the same directory.

## CSV Format
The CSV file should contain the following columns:
- headlines
- description
- category
