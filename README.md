# Machine-Learning-Project

This is the repository for Project 3 / Machine Learning (Steve Freeland).

My project involved the utilization of machine learning techniques to predict which feature is most likely to indicate potential fraud in an automobile insurance claim. 

## Data:

- Data was gathered from kaggle.com (insurance_claims.csv).
- Using Python Flask an API was built from the .csv database developed in Postgres.
- Utilized the following tools in development of this project: Scikit-Learn (sklearn), Python Pandas, Python Matplotlib, HTML/CSS/Bootstrap, JavaScript Plotly, and JavaScript D3.js.
- PostgreSQL utilized as SQL language with deployment on Heroku.

## Project Methodology:

- Fetch data from kaggle.com (https://www.kaggle.com/buntyshah/auto-insurance-claims-data)
- Data cleaning techniques: Dropped nulls and included/excluded select endpoints based on relevancy and type
- Data dump in PostgreSQL, utilizing schema diagrams to create data table
- Flask-based API generation: Utilized PostGres and Flask to read .csv file and build API (as well as front end web page with visualization)
- Data Science Machine Learning models used:
     - Random Forests consist of multiple single trees each based on a random sample of the training data. This results in a wide diversity that generally results in a better model. The feature fraud_reported was dropped from the list as this is the feature being predicted. After cleaning all remaining features were included.
     - Decision Trees build classification or regression models in the form of a tree structure. It breaks down a dataset into smaller subsets while at the same time an associated decision tree is incrementally developed. The feature fraud_reported was dropped from the list as this is the feature being predicted. After cleaning all remaining features were included.
- Host application via Heroku, modifying Project 2 approach / adding Summary Table and Tableau Public link

## High Level Findings:

- In terms of Random Forest importances, the highest-ranking feature is 'incident_severity_Major Damage'. Said another way and based on machine learning data, major damage is the most likely feature to be linked to fraud in an automobile insurance claim.
- Both algorithms utilized (Random Forests and Decision Trees) produced results supporting this finding (Random Forest accuracy of 0.794 and Decision Tree accuracy of 0.750). You can think of these measures as the percent of predictions that were correct.

## Users:	

- Please refer to config_example.bat file for understanding of required environment variables.

## Link to Heroku app:
https://auto-insurance-project.herokuapp.com/  

## Link to Final Project MSU Bootcamp Google Slides presentation:
https://docs.google.com/presentation/d/1EWcDqpivtcxxUCIFZQTf4gg4bIjmtGVe2vfMMDzKV6U/edit?usp=sharing
