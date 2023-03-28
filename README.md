This code scrape Shopee product titles from shopee.co.id. It can scrape multiple pages. This code is made by chatgpt 3. 

## Requirement:
- Python
- Selenium library

## How to use?
1. Simply run "Start.bat", then input keyword you want to search in shopee and hit enter.
2. You will get "hasil.txt" as a result containing all the headline that has been scraped.
3. In case you want to scrape more pages, simply change number "2" as your desired page number to scrape. Be mindful to not scraping too much as you will potentially get banned 

```python
# ulangi untuk 2 halaman
for p in range(2):
```
3. If you encounter slow network connection, edit the wait time longer. These number below are seconds.
```python
time.sleep(5)

SCROLL_PAUSE_TIME = 0.5
```


Thank You!