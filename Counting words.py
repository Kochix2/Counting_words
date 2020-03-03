import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter



def count_words(text):
    """
    Count the number of times each word occurs in text
    Skip the punctuation
    """
    text = text.lower()
    skip = [",",".",";",":","'",'"']
    for ch in skip:
        text = text.replace(ch,"")
    word_counts = {}
    for word in text.split(" "):
        
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
    


def count_words_fast(text):
    """
    Count the number of times each word occurs in text
    Skip the punctuation
    """
    skip = [",",".",";",":","'",'"']
    for ch in skip:
        text = text.replace('ch',"")
    
    word_counts = Counter(text.split(" "))
    return word_counts




def read_book(title_path):
    """
    Read a book and return it as a string
    """
    with open(title_path,"r",encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text


def word_stats(word_counts):
    """Return number of unique words and word frequences."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique,counts)


stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
Book_dir = "./Books"
for language in os.listdir(Book_dir):
    for author in os.listdir(Book_dir + "/" + language):
        for title in os.listdir(Book_dir + "/" + language + "/" + author):
            print(title)

            inputfile = Book_dir+ "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique,counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts) ,num_unique
            title_num += 1


subset = stats[stats.language == 'English']
plt.loglog(subset.length, subset.unique, "o", label="English", color = "crimson")

subset = stats[stats.language == 'Germany']
plt.loglog(subset.length, subset.unique, "o", label="Germany", color = "forestgreen")

subset = stats[stats.language == 'French']
plt.loglog(subset.length, subset.unique, "o", label="French", color = "orange")

subset = stats[stats.language == 'Portuguese']
plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color = "blueviolent")
plt.xlabel("Book of length")
plt.ylabel("unique words")
plt.sizefig("lang_plot.pdf")
  
    