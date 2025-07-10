# Sentimental-Analysis-Zepto


This project provides a Python script (`main.py`) for performing sentiment analysis on review text data, specifically targeting "Fast Delivery Agent Reviews" which is implied to be related to Zepto based on the file path in the code. It uses the `nltk` library's VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon to analyze sentiment and classifies reviews as Positive, Negative, or Neutral. The results, including sentiment scores, classifications, and percentages, are saved to an Excel file with conditional formatting applied to highlight sentiments for easy visualization.

## Features

* **Sentiment Analysis:** Utilizes `nltk.sentiment.vader` to analyze the sentiment of text reviews.
* **Sentiment Classification:** Classifies reviews into 'Positive', 'Negative', or 'Neutral' based on compound sentiment scores.
* **Sentiment Percentage Calculation:** Computes a percentage score for sentiment.
* **Excel Export with Formatting:** Saves the analyzed data to an Excel file, applying `lightgreen` for Positive, `lightcoral` for Negative, and `lightgrey` for Neutral sentiments in the 'Sentiment Classification' column.

## Requirements

Ensure you have the following Python dependencies installed:

```bash
pip install pandas nltk openpyxl
Key Dependencies:
•	Python 3.6+
•	pandas
•	nltk (Natural Language Toolkit)
•	openpyxl (for Excel operations, automatically installed by pandas for .xlsx output)
Installation
1.	Save the Script: Download or copy the main.py file to your desired project directory.
2.	Download NLTK VADER Lexicon: The script automatically attempts to download the vader_lexicon upon first run. If you encounter issues, you can run it manually:
Bash
python -m nltk.downloader vader_lexicon
3.	Prepare Your Dataset: Place your review dataset as a CSV file (e.g., Fast Delivery Agent Reviews.csv) in the location specified in the script (D:/original files for uplaoding/sentiment analysis zepto/Fast Delivery Agent Reviews.csv), or update the df = pd.read_csv(...) line in main.py with the correct path to your CSV file. Ensure the CSV has a column named Review Text.
Usage
1.	Run the Python script: Open your terminal or command prompt, navigate to the directory where main.py is located, and execute:
Bash
python main.py
2.	Check the Output: A new Excel file named Fast Delivery Agent Reviews 4 Sentiment Analysis.xlsx will be generated in the specified output path (D:/original files for uplaoding/sentiment analysis zepto/). This file will contain the original data along with 'Sentiment Score', 'Sentiment Classification', and 'Sentiment Percentage' columns, with the 'Sentiment Classification' column cells colored based on their sentiment.
Project Structure
/your-project-directory/
│── main.py                                  # Main Python script for sentiment analysis
│── Fast Delivery Agent Reviews.csv          # Example input dataset (as per script path)
│── Fast Delivery Agent Reviews 4 Sentiment Analysis.xlsx # Output Excel file
│── README.md                                # This documentation file
