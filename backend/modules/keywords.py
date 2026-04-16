from collections import Counter

def extract_keywords(text_list, top_n=5):
    # Combine all text
    words = " ".join(text_list).split()
    
    # Count frequency
    word_freq = Counter(words)
    
    # Get top keywords
    most_common = word_freq.most_common(top_n)
    
    return most_common