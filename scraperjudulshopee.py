from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time

# Keyword yang dicari
keyword = input("Masukkan keyword yang ingin dicari di shopee: ") 

# Inisialisasi driver
driver = webdriver.Chrome()
driver.maximize_window()

shopeesearch = "https://shopee.co.id/search?keyword="

# Gabungkan keyword dengan URL Shopee Search
formatted_keyword = quote(keyword)
url = shopeesearch + formatted_keyword

# buka file hasil.txt untuk menyimpan judul
file = open("hasil.txt", "w")

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
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/div[' + str(i+1) + ']/a/div/div/div[2]/div[1]/div/div')))
        file.write(title.text + "\n")

# tutup driver
driver.quit()
