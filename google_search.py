from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_search(query):
    print(" Opening browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")

    print(" Searching for:", query)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    print(" Waiting for results to load...")
    time.sleep(200)  # wait for results to load fully

    results = driver.find_elements(By.TAG_NAME, "h3")
    if not results:
        print(" No results found. Try increasing wait time or check selectors.")
    else:
        for i, result in enumerate(results[:200], start=1):
            print(f"{i}. {result.text}")

    driver.quit()
    print(" Search completed.")

if __name__ == "__main__":
    google_search("Python automation scripts")

