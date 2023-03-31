from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time
import csv
import os

nama_file = "../yang mau discrape.csv"
nama_produk = []

# membuka file csv
with open(nama_file, newline='') as file_csv:
    reader = csv.reader(file_csv)

    # membaca setiap baris data dan menyimpannya ke dalam variabel data
    for baris in reader:
        nama_produk.append(baris)

# Inisialisasi driver
driver = webdriver.Chrome()
driver.maximize_window()
    
for nm in nama_produk:

    # Keyword yang dicari
    keyword = nm[0] 
    
    print("\n Scraping headline -> " + keyword + "\n")
    
    shopeesearch = "https://shopee.co.id/search?keyword="

    # Gabungkan keyword dengan URL Shopee Search
    formatted_keyword = quote(keyword)
    url = shopeesearch + formatted_keyword
    
    if not os.path.exists("Hasil scrape"):
        os.makedirs("Hasil scrape")
    
    # buka file hasil.txt untuk menyimpan judul
    file = open("Hasil scrape/" + keyword + ".txt", "w")

    # ulangi untuk 2 halaman
    for p in range(2):

        # Buka halaman shopee.co.id
        driver.get(url + "&page=" + str(p))
        
        time.sleep(5)

        SCROLL_PAUSE_TIME = 0.5

        # Dapatkan tinggi browser saat ini
        browser_height = driver.execute_script("return window.innerHeight")

        # Dapatkan setengah tinggi browser
        half_browser_height = int(browser_height / 2)

        while True:
            # Dapatkan tinggi halaman saat ini
            current_height = driver.execute_script("return window.scrollY")

            # Scroll setengah tinggi browser ke bawah
            driver.execute_script("window.scrollBy(0, {});".format(half_browser_height))

            # Tunggu loading konten
            time.sleep(SCROLL_PAUSE_TIME)

            # Dapatkan tinggi halaman setelah scrolling
            new_height = driver.execute_script("return window.scrollY")

            # Jika tinggi halaman tidak berubah setelah scrolling, hentikan scrolling
            if new_height == current_height:
                break
                
        # ambil semua judul di halaman ini
        for i in range(60):
            try:
                title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/div[' + str(i+1) + ']/a/div/div/div[2]/div[1]/div/div')))
                
                # Untuk mengecek apakah headline produk shopee sama dengan yang dicari 
                title_lower = title.text.lower()              
                words = keyword.lower().split()
                
                if all(word in title_lower for word in words):
                    #print("true - " + title.text)
                    file.write(title.text + ", ")
                    
                else: print("Irrelevant Product - " + title.text)
                
            except UnicodeEncodeError:
                continue

# tutup driver
driver.quit()

print("scraperjudulshopee.py is Done!")
