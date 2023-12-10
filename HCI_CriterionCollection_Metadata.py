import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK models - punkt tokenizer
nltk.download('punkt')
nltk.download('popular')


# Ensure you've downloaded the NRC Emotion Lexicon and adjust the path below
nrc_lexicon_path = '/Users/trent/HCI_Prototype/NRC-Emotion-Lexicon/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt'

# Load the NRC Emotion Lexicon
emo_lexicon = pd.read_csv(nrc_lexicon_path, names=['word', 'emotion', 'association'], sep='\t')
emotion_words = set(emo_lexicon[emo_lexicon['association'] == 1]['word'])

# Function to extract emotion words
def extract_emotion_words(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() in emotion_words]
    return ', '.join(filtered_words)

# Load the input CSV file
df = pd.read_csv('/Users/trent/HCI_Prototype/criterion_collection.csv')

# Apply the function to the 'Description' column (assumed to be column C)
df['terms_separated'] = df.iloc[:, 2].apply(extract_emotion_words)

# Save to a new CSV file
df.to_csv('/Users/trent/HCI_Prototype/criterion_collection_metadata.csv', index=False)

