<!-- SHIELDS -->
[![Colab][colab-shield]][colab-url]
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![Linkedin][linkedin-shield]][linkedin-url]


<!-- PROJECT INTRO -->
<br />
<div align="center">
  <h2 align="center">SJR-Journal-Ranking</h2>

  <p align="center">
    A web scraping and visualization project on SJR and WoS journal indexes.
    <br />
    <a href="https://public.tableau.com/app/profile/abir.hassan/viz/SJRJournalRankingAnalysis/Dashboard1">View Dashboard</a>
    ·
    <a href="https://github.com/abir0/SJR-Journal-Ranking/issues">Report Bug</a>
    ·
    <a href="https://github.com/abir0/SJR-Journal-Ranking/issues">Request Feature</a>
  </p>
</div>

<p align="center">
  <img src="images/dash1.png" width="800" />
</p>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#problem-statement">Problem Statement</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#results">Results</a></li>
  </ol>
</details>

<br>


## Problem Statement

This project is a data scraping, analysis, and visualization project on Research Journals. The project is divided into two parts: the first part is the web scraping part, which is done using Selenium and Python; the second part is the data analysis and visualization part, which is done using Tableau. The project is done as a part of the 1st capstone project of MasterCourse Data Science Cohort 2 program.

The data is scraped from the following websites:

* [Scimago Journal Ranking (SJR)](https://www.scimagojr.com/journalrank.php?wos=true&type=j)
* [Web of Science (WoS)](https://mjl.clarivate.com/search-results)

An external dataset is also used in this project:
* [Scopus](https://www.scopus.com/sources.uri)

<p float="left" align="center">
  <img src="images/scj.png" width="400" />
  <img src="images/wos.png" width="400" />
</p>

From these 3 sources, the following information is scraped:

* Journal Name or Title
* Subject Area
* Open Access
* Publisher
* Country
* Coverage Year
* Journal Rank
* SJR Index
* Quartile
* H-Index
* CiteScore
* References Count
* Citations Count
* Documents Count

The scraped data is then cleaned and analyzed using Python libraries such as Pandas, Numpy, Matplotlib, and Seaborn. The cleaned data is then visualized using Tableau. The final dashboard can be found [here][dashboard-url].



### Built With

Python libraries and softwares used in this project:

* [![Selenium][Selenium]][Selenium-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Numpy][Numpy]][Numpy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Seaborn][Seaborn]][Seaborn-url]
* [![Tableau][Tableau]][Tableau-url]



<!-- INSTALLATION -->
## Installation

This project is done using Python 3.11.0. Please install the latest version of Python before running the project.

Below are the steps to run the project:

1. Clone the repo
```bash
git clone https://github.com/abir0/SJR-Journal-Ranking.git
```

2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads and add the path to the `chromedriver.exe` file in PATH environment variable.

5. Run the scraper scripts
```bash
python src/sjr_scraper.py
python src/wos_scraper.py
```

1. Run all the cells in the data transformation and analysis notebook in google colab or download the notebook and run it in Jupyter.

2. You will get a file named `combined_journal_ranking_data.csv`. This is the final data.

3. Open the `SJR and WoS Journal Ranking.twb` file in Tableau and connect the `combined_journal_ranking_data.csv` file to the workbook.


## Results

The final dashboard can be found [here][dashboard-url].

Here are some of the visualizations from the dashboard:

### Dashboard 1

<p align="center">
  <img src="images/dash1.png" width="800" />
</p>

### Dashboard 1

<p align="center">
  <img src="images/dash2.png" width="800" />
</p>


Key findings from the analysis:

* From the correlation analysis, it is found that there is a positive correlation between SJR Index and CiteScore, H-index, and Cites per Docs. So these metrics are better indicators than the simple counts of citations, references, and documents.
* But as the rank of the journal increases, those better metrics fall short.
* Based on CiteScore, top 5 publishers are: Wiley, Elsevier, Springer, Nature Portfolio, and Routledge. Reflecting their high quality of journals.
* One interesting observation: based on the number of documents, citations, and references MDPI is among the top 5 publishers. This is because MDPI publishes a lot of journals, but the quality of the journals are not as high as the top 5 publishers which is reflected by the poor CiteScore.
* Open Access journals have a higher Avg. Cites per Docs than non-Open Access journals.
* The top 5 journals with the highest SJR index are: Nature Reviews Materials, Nature Reviews Drug Discovery, Nature Reviews Molecular Cell Biology, Nature Reviews Cancer, and Nature Reviews Genetics.
* The top 5 countries with the highest number of journals are: United States, United Kingdom, Netherlands, Germany, and Switzerland.
* Top 2 subject areas with the highest H-index are: Medicine and Social Sciences.




<!-- MARKDOWN LINKS & IMAGES -->
[dashboard-url]: https://public.tableau.com/app/profile/abir.hassan/viz/SJRJournalRankingAnalysis/Dashboard1
[colab-shield]: https://colab.research.google.com/assets/colab-badge.svg
[colab-url]: https://colab.research.google.com/drive/1Fj1eJKqB_Y9wDbKTx16AKk2q7X9hLoOh?usp=sharing
[contributors-shield]: https://img.shields.io/github/contributors/abir0/SJR-Journal-Ranking.svg
[contributors-url]: https://github.com/abir0/SJR-Journal-Ranking/graphs/contributors
[license-shield]: https://img.shields.io/github/license/abir0/SJR-Journal-Ranking.svg
[license-url]: https://github.com/abir0/SJR-Journal-Ranking/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/abir0

[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Seaborn]: https://img.shields.io/badge/Seaborn-%23000000.svg?style=for-the-badge&logo=Matplotlib&logoColor=blue
[Tableau]: https://img.shields.io/badge/Tableau-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Selenium-url]: https://www.selenium.dev/
[Pandas-url]: https://pandas.pydata.org/
[Numpy-url]: https://numpy.org/
[Matplotlib-url]: https://matplotlib.org/
[Seaborn-url]: https://seaborn.pydata.org/
[Tableau-url]: https://public.tableau.com/app/discover