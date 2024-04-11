# About Dataset

## Source
[Kaggle](https://www.kaggle.com/datasets/samanemami/market-research-survey?resource=download)

## Context
This is a demographic survey conducted by the market research department. The focus of this dataset is to have the customers' preferences regarding the computer brand.

## Content
This dataset includes the complete_responses.csv that is the training split and survey_incomplete.csv for the test split. The training part consists of almost 10,000 answered surveys. The survey key is inside the survey_key.csv

| Column | Data type | Description |
|---|---|---|
| salary | float | Salary of a person in float format (up to the last 5 digits) |
| age | int | Age of the corresponded person |
| elevel | Int | Highelst level of education, ranging from 0 to 4 (check in `survey_key.txt` for more details |
| car | int | Primary car used by the person, ranging from 1 to 20 correspond to car brand (check in `survey_key.txt` for more details) |
| zipcode | int | Zipcode representing regions in the U.S (check in `survey_key.txt` for more details) |
| credit | float | Amount of credit available |
| brand | int | Value is 0 and 1, 0 for Acer and 1 for Sony |
