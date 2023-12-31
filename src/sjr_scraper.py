import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# URL parameters
params = {
    "wos": "true",
    "type": "j",
    "year": "2022",
}

# Subject areas and their ids
subject_areas = {
    1100: "Agricultural and Biological Sciences",
    1200: "Arts and Humanities",
    1300: "Biochemistry, Genetics and Molecular Biology",
    1400: "Business, Management and Accounting",
    1500: "Chemical Engineering",
    1600: "Chemistry",
    1700: "Computer Science",
    1800: "Decision Sciences",
    3500: "Dentistry",
    1900: "Earth and Planetary Sciences",
    2000: "Economics, Econometrics and Finance",
    2100: "Energy",
    2200: "Engineering",
    2300: "Environmental Science",
    3600: "Health Professions",
    2400: "Immunology and Microbiology",
    2500: "Materials Science",
    2600: "Mathematics",
    2700: "Medicine",
    1000: "Multidisciplinary",
    2800: "Neuroscience",
    2900: "Nursing",
    3000: "Pharmacology, Toxicology and Pharmaceutics",
    3100: "Physics and Astronomy",
    3200: "Psychology",
    3300: "Social Sciences",
    3400: "Veterinary",
}


def get_url_with_params(url, params):
    return url + "?" + "&".join([key + "=" + value for key, value in params.items()])


def parse_best_categories(text):
    categories = text.split(":")[1][:-1].split(";")
    return [category.strip() for category in categories]


def get_row_data(row):
    cells = row.find_elements(By.TAG_NAME, "td")
    contents = {}
    contents["Rank"] = cells[0].text
    contents["Title"] = cells[1].text
    contents["Open Access"] = cells[1].find_elements(By.TAG_NAME, "img") != []
    contents["URL"] = str(cells[1].find_element(By.TAG_NAME, "a").get_attribute("href")) + "/"
    cell_3 = cells[3].text.split()
    if len(cell_3) > 1:
        contents["SJR index"] = cell_3[0]
        contents["Best Quartile"] = cell_3[1]
        contents["Best Categories"] = parse_best_categories(
            cells[3].find_element(By.TAG_NAME, "span").get_attribute("title"))
    else:
        contents["SJR index"] = None
        contents["Best Quartile"] = None
        contents["Best Categories"] = None
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
    URL = "https://www.scimagojr.com/journalrank.php"

    # Output filename
    filename = "data/sjr_journal_ranking_{}.csv".format(params["year"])

    # Initialize the driver
    driver = webdriver.Chrome()

    # Iterate over the subject areas
    for subject_area_id, subject_area_name in subject_areas.items():
        journal_data = []
        params["area"] = str(subject_area_id)

        next_page_exists = True
        page_number = 1

        while next_page_exists:
            # Get the page with the params
            params["page"] = str(page_number)
            driver.get(get_url_with_params(URL, params))

            # Get the table rows
            rows = driver.find_elements(By.TAG_NAME, "tr")[1:]

            # Iterate over the rows and scrape the table data
            for row in rows:
                row_contents = get_row_data(row)
                row_contents["Subject Area"] = subject_area_name
                journal_data.append(row_contents)

            # Check if there is a next page
            next_button = driver.find_elements(
                By.CLASS_NAME, "pagination_buttons")[0].find_elements(By.TAG_NAME, "a")[1]
            if next_button.get_attribute("class") == "disabled":
                next_page_exists = False
            page_number += 1

        print(subject_area_name, len(journal_data))

        # Save the data to a file
        df = pd.DataFrame(journal_data)
        if subject_area_id == 1100:
            # For the first subject area, create a new file
            df.to_csv(filename, index=False)
        else:
            # For the rest, append to the existing file
            df.to_csv(filename, mode="a", index=False, header=False)

        # Free up memory
        del journal_data, df

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
