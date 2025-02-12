# Data-Pipeline-Automation
Make an Data Pipeline Automation for Data Engineer Jobs listing from Glassdoor using Apache Airflow then connecting it to MongoDB.

## Overview

This project automates the extraction, transformation, and storage of Data Engineer job listings from Glassdoor. The pipeline is orchestrated using Apache Airflow and stores the processed data in MongoDB for further analysis.

## Features
- Data Extraction               : Extract dataset from kaggle 'job listings from Glassdoor'.
- Data Cleaning & Transformation: Uses Pandas and PySpark for data processing. 
- Data Quality Assurance        : Implements validation with Great Expectations.
- ETL Orchestration             : Managed with Apache Airflow.
- Containerized Deployment      : Utilizes Docker for easy deployment.
- NoSQL Storage                 : Stores processed data in MongoDB.

## Technologies & Tools
- Python            : Core programming language.
- Pandas & PySpark  : Data manipulation and transformation.
- Apache Airflow    : Workflow orchestration.
- Great Expectations: Data validation.
- Docker            : Containerized execution.
- MongoDB           : NoSQL database for storage.

## Data Source
Kaggle.com → Data Engineer Job Listing from glassdor

## Usage
- build docker using docker `docker build -t airflow-spark .`
- run docker compose using `docker compose -f airflow.yaml up`
- when running the airflow, use this to enable pyspark `sudo -u airflow python script.py`

1. Start the Airflow web server and scheduler.
2. Trigger the DAG for job listings extraction and processing.
3. Monitor the pipeline execution via the Airflow UI.
4. Query the processed data in MongoDB for analysis.

## Disclaimer
This project is for educational purposes only. Ensure compliance with data usage policies and privacy regulations.

## Author

Daniswara Eka Saputra

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniswaraekas/)