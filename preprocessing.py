import pandas as pd
import re

def remove_emojis(text):
    emoji_pattern = re.compile(
        "[" 
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese characters
        u"\U00002702-\U000027B0"  # various symbols
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_new_lines(text):
    return text.replace('\n', ' ')

def remove_username(text):
  username_pattern = re.compile('\xa0.*\xa0')
  return username_pattern.sub(r'',text)


# Function to extract comments and remove emojis
def extract_comments_without_emojis(df):
    if 'comment' not in df.columns:
        raise ValueError("DataFrame must contain a 'comment' column")
    
    # Extract the 'comment' column and remove emojis
    cleaned_comments = df['comment'].apply(remove_emojis)\
    .apply(remove_new_lines)\
    .apply(remove_username).to_list()

    cleaned_comments = [comment for comment in cleaned_comments if comment!='']
    
    return cleaned_comments
