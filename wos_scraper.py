import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_card_data(card):
    contents = {}
    try:
        contents["Title"] = card.find_element(By.TAG_NAME, "mat-card-title").text.strip()
    except:
        return None
    card_values = card.find_elements(By.CLASS_NAME, "search-results-value")
    try:
        publisher, address = card_values[0].text.strip().split(",", 1)
    except ValueError:
        publisher = card_values[0].text.strip()
        address = ""
    except IndexError:
        return None
    contents["Publisher"] = publisher.strip()
    contents["Address"] = address.strip()
    try:
        contents["Core Collection"] = card_values[2].text.strip()
    except IndexError:
        contents["Core Collection"] = "Additional Indexes"
    return contents


def main():
    URL = "https://mjl.clarivate.com/search-results"

    # Initialize the driver
    driver = webdriver.Chrome()

    driver.get(URL)

    # Select the options
    # Sort by: Title (A-Z)
    driver.find_elements(By.TAG_NAME, "mat-form-field")[-2].click()
    time.sleep(3)
    driver.find_elements(By.TAG_NAME, "mat-option")[1].click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Items per page: 50
    driver.find_elements(By.TAG_NAME, "mat-form-field")[-1].click()
    time.sleep(2)
    driver.find_elements(By.TAG_NAME, "mat-option")[2].click()
    time.sleep(2)

    wos_data = []
    next_page_exists = True

    while next_page_exists:
        # Get the cards from the search results
        cards = driver.find_element(
            By.TAG_NAME, "app-journal-search-results").find_elements(
            By.TAG_NAME, "mat-card")

        # Iterate over the card elements
        for card in cards:
            wos_data.append(get_card_data(card))

        # Check if there is a next page
        driver.find_element(
            By.CLASS_NAME, "mat-paginator-range-actions").find_elements(
            By.TAG_NAME, "button")[2].click()

        paginator_element = EC.presence_of_element_located((
            By.CLASS_NAME, "mat-paginator-range-actions"))
        WebDriverWait(driver, 12).until(paginator_element)

        if driver.find_element(
                By.CLASS_NAME, "mat-paginator-range-actions").find_elements(
                By.TAG_NAME, "button")[2].get_attribute("disabled"):
            next_page_exists = False

    # Save the data to a file
    df = pd.DataFrame(wos_data)
    df.to_csv("wos_master_journal_list.csv", index=False)

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
