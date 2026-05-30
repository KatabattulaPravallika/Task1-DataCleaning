# Task 1 - Data Cleaning and Preprocessing

## Objective

The objective of this task is to clean and preprocess a raw dataset by handling missing values, checking duplicate records, standardizing column names, and converting data types into appropriate formats.

## Dataset

Customer Personality Analysis (marketing_campaign.csv)

## Tools Used

* Python
* Pandas
* Visual Studio Code

## Data Cleaning Steps Performed

### 1. Loaded Dataset

Loaded the dataset using Pandas.

### 2. Handled Missing Values

* Identified missing values using `isnull()`.
* Found 24 missing values in the Income column.
* Replaced missing values with the mean Income value.

### 3. Checked Duplicate Records

* Checked for duplicate rows using `duplicated()`.
* No duplicate records were found.

### 4. Standardized Column Names

* Converted all column names to lowercase for consistency.

### 5. Converted Data Types

* Converted the `dt_customer` column from string format to datetime format.

### 6. Saved Cleaned Dataset

* Saved the cleaned dataset as `cleaned_marketing_campaign.csv`.

## Files Included

* marketing_campaign.csv (Original Dataset)
* cleaned_marketing_campaign.csv (Cleaned Dataset)
* task1.py (Python Code)
* summary.txt (Task Summary)
* README.md (Project Documentation)

## Outcome

The dataset was successfully cleaned and prepared for further analysis.
