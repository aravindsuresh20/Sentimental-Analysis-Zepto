import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Load the data
df = pd.read_csv('D:/original files for uplaoding/sentiment analysis zepto/Fast Delivery Agent Reviews.csv')

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Analyze sentiment
df['Sentiment Score'] = df['Review Text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])

# Classify sentiment
df['Sentiment Classification'] = df['Sentiment Score'].apply(
    lambda x: 'Positive' if x >= 0.05 else 'Negative' if x <= -0.05 else 'Neutral'
)

# Sentiment percentage
df['Sentiment Percentage'] = df['Sentiment Score'].apply(lambda x: f"{(x + 1) * 50:.2f}%")

# Apply color formatting
def highlight_sentiment(val):
    color = 'background-color: '
    if val == 'Positive':
        color += 'lightgreen'
    elif val == 'Negative':
        color += 'lightcoral'
    else:
        color += 'lightgrey'
    return color

styled = df.style.applymap(highlight_sentiment, subset=['Sentiment Classification'])

# Save to Excel
styled.to_excel('D:/original files for uplaoding/sentiment analysis zepto/Fast Delivery Agent Reviews 4 Sentiment Analysis.xlsx', index=False, engine='openpyxl')
print("Sentiment analysis completed and saved with color formatting.")
