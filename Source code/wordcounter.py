import re
import os

print("wordcounter.py is Running!")

# mendapatkan daftar file dalam folder
file_list = os.listdir('Hasil scrape')

# menampilkan daftar file
for file_name in file_list:
    with open("Hasil scrape/" + file_name, "r") as file:
        text= file.read()

    # Menghilangkan semua karakter selain huruf dan angka
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    # Convert all characters to lowercase to ignore case sensitivity
    text = text.lower()

    # Split the text into individual words
    words = text.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Loop through the words and update the dictionary
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Mengurutkan kamus berdasarkan nilai hitungan kata dari yang paling banyak ke paling sedikit
    word_counts_sorted = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    kata_terbanyak = []
    
    if not os.path.exists("Word counter"):
        os.makedirs("Word counter")
        
    # Menampilkan hitungan kata yang diurutkan
    for word, count in word_counts_sorted.items():
        kata_terbanyak.append(word)
    
    with open('Word counter/' + file_name, "w") as f:
        for kata in kata_terbanyak:
            f.write(kata + ", ")
        
print("wordcounter.py is Done!")