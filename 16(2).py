import matplotlib as plt
import requests
import numpy as np
import pylab

word = input("Enter word: ").lower()
print(word)

pages = []
for i in range(1, 9):
    res = input(f"url sites {i}: ")
    pages.append(res)
print(pages)

counts = []

for url in pages:
    responce = requests.get(url).text
    text_p = responce.lower().count(word)
    counts.append(text_p)
    print(f"Your word is {word}. We are find {text_p} in page {url}")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array(counts)

pylab.bar(x, y)
pylab.show()

