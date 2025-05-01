# Dmart Sales Data Analysis using PySpark

## Overview

This project focuses on building a data pipeline using PySpark to integrate and analyze sales data from Dmart. It involves loading data from three different CSV files (product information, sales transactions, and customer details), performing data transformations and cleaning, and then answering a set of analytical questions to gain insights into the sales patterns.

## Technologies Used

* **Python:** The primary programming language.
* **PySpark:** A powerful framework for large-scale data processing.
* **SQL:** Used within PySpark for querying and data manipulation.

## Dataset

The project utilizes the "Dmart" dataset, which is comprised of the following CSV files:

* `products.csv`: Contains information about the products.
* `sales.csv`: Contains details about the sales transactions.
* `customer.csv`: Contains information about the customers.

## Problem Statement

The primary goal is to create a robust data pipeline using PySpark to effectively integrate and analyze sales data from various sources. This analysis aims to answer key business questions related to product performance, customer behavior, and overall sales trends.

## Tasks

The project is structured into the following key tasks:

**Task 1: Establish PySpark Connection**

* Set up a PySpark environment.
* Create a SparkSession to interact with PySpark.

**Task 2: Load Data into PySpark DataFrames**

* Load the `products.csv`, `sales.csv`, and `customer.csv` files into separate PySpark DataFrames.

**Task 3: Data Transformation and Cleaning**

* Perform necessary data cleaning and transformation:
    * Rename columns for consistency (if required).
    * Handle missing values appropriately based on the data context.
    * Ensure the correct data types are assigned to each column for accurate analysis.
* Join the DataFrames on relevant keys:
    * Join the `products` and `sales` DataFrames using the `Product ID` as the key.
    * Join the resulting DataFrame with the `customer` DataFrame using the `Customer ID` as the key.

**Task 4: Data Analysis and Querying**

* Formulate analytical questions to extract meaningful insights from the integrated dataset.
* Write PySpark code (using either PySpark DataFrame API or Spark SQL) to answer these questions.

**Task 5: Run Queries on the Pyspark**

The following analytical questions are addressed:

1.  **What is the total sales for each product category?**
2.  **Which customer has made the highest number of purchases?**
3.  **What is the average discount given on sales across all products?**
4.  **How many unique products were sold in each region?**
5.  **What is the total profit generated in each state?**
6.  **Which product sub-category has the highest sales?**
7.  **What is the average age of customers in each segment?**
8.  **How many orders were shipped in each shipping mode?**
9.  **What is the total quantity of products sold in each city?**
10. **Which customer segment has the highest profit margin?**

## Getting Started

To run this project, you will need:

* **Python 3.x** installed on your system.
* **Apache Spark** set up and configured (with PySpark).
* The `products.csv`, `sales.csv`, and `customer.csv` files in a location accessible to your PySpark environment.

### Installation

1.  **Install PySpark:**

    ```bash
    pip install pyspark
    ```

2.  **Set up Spark:**

    * Download Apache Spark from the official website.
    * Follow the installation instructions for your operating system.
    * Ensure that the `SPARK_HOME` environment variable is set correctly.

3.  **Clone the repository (if applicable):**

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

4.  **Place the datasets:**

    Ensure that the `products.csv`, `sales.csv`, and `customer.csv` files are in the same directory as your PySpark script or provide the correct file paths in your code.

### Usage

1.  **Run the PySpark script:**

    You will have a Python script (e.g., `dmart_analysis.py`) that contains the PySpark code for loading, transforming, and querying the data. Execute this script using `spark-submit`:

    ```bash
    spark-submit dmart_analysis.py
    ```

    (Replace `dmart_analysis.py` with the actual name of your script).

2.  **View the results:**

    The script will process the data and print the answers to the analytical questions on the console.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your forked repository.
5.  Submit a pull request.
