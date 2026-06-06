# natural_language_processing

## Project Overview
This repository contains a comprehensive suite of Natural Language Processing (NLP) implementations and web scraping utilities. It covers fundamental NLP preprocessing techniques, feature extraction methods, and a robust SMS spam detection system. Additionally, it includes advanced web scraping scripts designed to collect historical weather data.

## Deep Technical Details

### 1. Natural Language Processing (NLP)
The repository implements a modular approach to text processing and classification:
- **Text Preprocessing:** Robust cleaning pipelines using `Regex` for noise removal, alongside `NLTK` for Tokenization, Stemming (Porter Stemmer), and Lemmatization (WordNet Lemmatizer).
- **Feature Engineering:** 
  - **Bag of Words (BoW):** Utilizing `CountVectorizer` to transform text into numerical vectors.
  - **TF-IDF:** Implementing `TfidfVectorizer` for importance-based word weighting.
- **Classification Model:** A high-accuracy SMS Spam Detection system built using the **Multinomial Naive Bayes (MultinomialNB)** algorithm from `Scikit-learn`. The pipeline involves text cleaning, vectorization, and model training/evaluation, achieving a reported accuracy of ~98.2%.

### 2. Web Scraping Pipeline
The `web_scrapping` module focuses on automated data extraction:
- **Dynamic Content Handling:** Uses `Selenium WebDriver` to navigate and interact with `timeanddate.com`.
- **Data Extraction:** Iteratively scrapes historical weather metrics including:
    - Temperature
    - Wind Speed
    - Humidity
    - Atmospheric Pressure
    - Visibility
- **Automation:** Scripts are designed to handle multi-year and multi-month data ranges, with built-in error handling and `time.sleep` intervals to manage request throttling.

## Tech Stack
- **Languages:** Python
- **NLP Libraries:** NLTK, Regex
- **Machine Learning:** Scikit-learn (Naive Bayes, Vectorizers, Metrics)
- **Data Manipulation:** Pandas, NumPy
- **Web Scraping:** Selenium, CSV
- **Notebooks:** Jupyter Notebook (.ipynb)
