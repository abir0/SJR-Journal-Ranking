import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_best_categories(text):
    categories = text.split(":")[1][:-1].split(";")
    return [category.strip() for category in categories]


def get_row_data(row):
    cells = row.find_elements(By.TAG_NAME, "td")
    contents = {}
    contents["Overall Rank"] = cells[0].text
    contents["Title"] = cells[1].text
    contents["URL"] = cells[1].find_element(By.TAG_NAME, "a").get_attribute("href")
    contents["Open Access"] = cells[1].find_elements(By.TAG_NAME, "img") != []
    contents["SJR index"] = cells[3].text.split()[0]
    contents["Best Quartile"] = cells[3].text.split()[1]
    contents["Best Categories"] = parse_best_categories(
        cells[3].find_element(By.TAG_NAME, "span").get_attribute("title"))
    contents["H index"] = cells[4].text
    contents["Total Docs."] = cells[5].text
    contents["Total Docs. 3y"] = cells[6].text
    contents["Total Refs."] = cells[7].text
    contents["Total Cites 3y"] = cells[8].text
    contents["Citable Docs. 3y"] = cells[9].text
    contents["Cites/Doc. 2y"] = cells[10].text
    contents["Refs./Doc."] = cells[11].text
    contents["Country"] = cells[12].find_element(By.TAG_NAME, "img").get_attribute("title")
    return contents


def main():
    URL = "https://www.scimagojr.com/journalrank.php?wos=true&type=j&year=2022&page={}"

    driver = webdriver.Chrome()

    journal_data = []

    next_page_exists = True
    page_number = 1

    while next_page_exists:
        driver.get(URL.format(page_number))

        # Scrape the table rows
        rows = driver.find_elements(By.TAG_NAME, "tr")[1:]
        
        for row in rows:
            # Scrape the table data
            journal_data.append(get_row_data(row))
        
        # Check if there is a next page
        next_page_exists = driver.find_elements(By.CLASS_NAME, "pagination_buttons")[1].get_attribute("href") != "#"
        page_number += 1

    driver.quit()

    print(len(journal_data))

    # Save the data to a file
    df = pd.DataFrame(journal_data)
    df.to_csv("sjr_journal_ranking.csv", index=False)


if __name__ == "__main__":
    main()
