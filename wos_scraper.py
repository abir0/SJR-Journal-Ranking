import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_card_data(card):
    contents = {}
    contents["Title"] = card.find_element(By.TAG_NAME, "mat-card-title").text.strip()
    card_values = card.find_elements(By.CLASS_NAME, "search-results-value")
    contents["Publisher"], contents["Address"] = card_values[0].text.strip().split(",", 1)
    contents["Core Collection"] = card_values[2].text.strip()
    return contents


def main():
    URL = "https://mjl.clarivate.com/search-results"

    filename = "wos_master_journal_list.csv"

    wos_data = []

    # Initialize the driver
    driver = webdriver.Chrome()

    driver.get(URL)

    # Select the options
    driver.find_elements(By.TAG_NAME, "mat-form-field")[-2].click()
    time.sleep(3)
    driver.find_elements(By.TAG_NAME, "mat-option")[1].click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_elements(By.TAG_NAME, "mat-form-field")[-1].click()
    time.sleep(2)
    driver.find_elements(By.TAG_NAME, "mat-option")[2].click()
    time.sleep(2)

    next_page_exists = True

    while next_page_exists:
        time.sleep(2)
        elements = driver.find_element(
            By.TAG_NAME, "app-journal-search-results").find_elements(
            By.TAG_NAME, "mat-card")
        print(len(elements))

        # Iterate over the rows and scrape the table data
        for element in elements:
            wos_data.append(get_card_data(element))

        # Check if there is a next page
        driver.find_element(
            By.CLASS_NAME, "mat-paginator-range-actions").find_elements(
            By.TAG_NAME, "button")[2].click()
        time.sleep(2)
        if driver.find_element(
                By.CLASS_NAME, "mat-paginator-range-actions").find_elements(
                By.TAG_NAME, "button")[2].get_attribute("disabled"):
            next_page_exists = False

    # Save the data to a file
    df = pd.DataFrame(wos_data)
    df.to_csv(filename, index=False)

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
