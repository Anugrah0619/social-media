from collections import Counter

def extract_keywords(text_list, top_n=5):
    words = " ".join(text_list).split()
    
    # Remove small/weak words
    words = [w for w in words if len(w) > 3]

    word_freq = Counter(words)
    
    most_common = word_freq.most_common(top_n)
    
    return most_common