##########################################################
# Nik Pevnev
# 4/27/2025
# ----------------
# Top Nouns Extractor and Visualizer
# This script parses a given text, identifies the top 25 nouns, and plots them
# in a horizontal bar chart with the frequency axis shown at the top.
# 
# Features:
# - Text parsing using spaCy
# - Top 25 noun extraction
# - Horizontal bar chart visualization (frequency axis on top)
#
# Usage: python3 top_nouns.py
#
# Example:
# python3 top_nouns.py
#
# Dependencies:
# - spaCy: Natural Language Processing library
# - Matplotlib: Data visualization library
# - Python 3.x (Tested on Python 3.8+)
#
# Tested on:
# - Linux (Ubuntu 20.04)
# - Windows 10
#
# Disclaimer:
# This script is for educational purposes only and should be used legally and ethically.
# The author is not responsible for any misuse or damage caused by this script.
# Use it at your own risk.
#
# GitHub:
# https://github.com/nikpevnev
#
# Credits:
# - spaCy: https://spacy.io/
# - Matplotlib: https://matplotlib.org/
# - Python: https://www.python.org/
#
# License:
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
##########################################################
# Note: This script requires internet access if the spaCy model needs to be downloaded.
##########################################################

import spacy
import matplotlib.pyplot as plt
from collections import Counter

# Load the spaCy model (you might need to download it first: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

def plot_top_nouns(text):
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    noun_counts = Counter(nouns)
    top_nouns = noun_counts.most_common(25)  # Get the top 25 nouns

    # Prepare data for plotting
    labels, values = zip(*top_nouns)

    # Create a bar chart
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    plt.barh(labels, values, color='skyblue') # Horizontal bar chart
    plt.xlabel("Frequency")
    plt.ylabel("Nouns")
    plt.title("Top 25 Nouns in Job Description")
    plt.gca().xaxis.set_label_position('top')
    plt.gca().xaxis.tick_top()
    plt.gca().invert_yaxis() # Invert y axis to show most frequent at the top

    plt.tight_layout() # Adjust layout
    plt.show()

# Example usage:
example_text = """Job Description goes here
"""
plot_top_nouns(example_text)