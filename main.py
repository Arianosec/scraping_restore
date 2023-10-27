from bs4 import BeautifulSoup
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def get_data_with_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    try:
        item_list = []
        for i in range(1, 9):
            count = 0
            url = f"https://re-store.ru/apple-iphone/?page={i}"
            driver.get(url=url)
            cards = driver.find_elements(By.CLASS_NAME, "catalog__product")
            for item in cards:
                if count % 4 == 0:
                    driver.execute_script("window.scrollBy(0,400)")
                image = item.find_element(By.TAG_NAME, "img").get_attribute("src")
                name = item.find_element(By.CLASS_NAME, "product-card__title").text
                price = item.find_element(By.CLASS_NAME, "product-card__price-new").text
                item_list.append(
                    {
                        "Image": image,
                        "Name": name,
                        "Price": price
                    }
                )
                count += 1
        with open("item_list.append.json", "a", encoding="utf-8") as file:
            json.dump(item_list, file, indent=4, ensure_ascii=False)
        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:
            driver.close()
            driver.quit()
def main():
    get_data_with_selenium()
if __name__ == "__main__":
    main()