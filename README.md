# Machine-Learning-Project

This is the repository for Project 3 / Machine Learning (Steve Freeland).

My project involved the utilization of machine learning techniques to predict which factor(s) is most likely to indicate potential fraud in an automobile insurance claim. 

## Data:

- Data was gathered from kaggle.com (insurance_claims.csv).
- Using Python Flask an API was built from the .csv database developed in PostGres.

## Project Steps:

- Creation of a PostGres SQL database table built from the kaggle .csv file.
- Incorporated Python Flask to create API from the .csv data.
- D3 and chart.js tool utilized to develop front end, thereby allowing for the query and presentation of API data.
- Machine Learning: Machine learning is a field of study concerned with algorithms that learn from examples.
- For my project, I utilized Random Forest and Decision Tree machine learning algorithms to determine which factor(s) is most likely to predict fraud in auto insurance claims. 
- Deployed project via Heroku.

## High Level Findings:

- In terms of Random Forest importances, the highest-ranking factor is 'incident_severity_Major Damage'. Said another way and based on machine learning data, major damage is the most likely factor to be linked to fraud in an automobile insurance claim.

## Users:

- Please refer to config_example.bat file for understanding of required environment variables.
