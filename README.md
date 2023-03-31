This code scrape Shopee product titles from shopee.co.id. It can scrape multiple pages. This code is made by chatgpt 3. 

## Requirement:
- Python
- Selenium library

## How to use?
1. Put product name that you want to scrape at "yang mau discrape.csv". Simply open with Ms. Excel and put product name at "Column A". You can scrape multiple product name at the same time. Just put each product in new line, no need comma.

2. Run "Start.bat" and wait till the process done.

3. You will get your result inside folder /Source code/Hasil scrape

4. I also make wordcounter.py to count the most word used for a product. I will use that as a refference for my own product headline. The result of wordcounter.py is inside folder /Source code/Word counter.

5. In case you want to scrape more pages, simply change number "2" as your desired page number to scrape. Be mindful to not scraping too much as you will potentially get banned. Edit file "scraperjudulshopee.py" inside Source code folder.

```python
# ulangi untuk 2 halaman
for p in range(2):
```

6. If you encounter slow network connection, edit the wait time longer. These numbers below are in seconds. Edit file "scraperjudulshopee.py" inside Source code folder.

```python
time.sleep(5)

SCROLL_PAUSE_TIME = 0.5
```
## Note
This code scrapes product that relevant to your search. Sometimes shopee show irrelevant product when you search specific keyword. We fix that using "if all" code, so that we scrape product headline that contain words you put inside "yang mau discrape.csv". 

Thank You!