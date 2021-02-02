# Machine-Learning-Project

This is the repository for Project 3 / Machine Learning (Steve Freeland).

My project involved the utilization of machine learning techniques to predict which feature(s) is most likely to indicate potential fraud in an automobile insurance claim. 

## Data:

- Data was gathered from kaggle.com (insurance_claims.csv).
- Using Python Flask an API was built from the .csv database developed in Postgres.
- Utilized the following tools in development of this project: scikit learn (sklearn), Python/Pandas, Matplotlib, HTML/CSS/Bootstrap, JavaScript, Plotly, and D3.js.
- PostgreSQL utilized as SQL language with deployment on Heroku.

## Project Steps:

- Creation of a PostgreSQL database table built from the kaggle .csv file.
- Incorporated Python Flask to create API from the .csv data.
- D3 and chart.js tool utilized to develop front end, thereby allowing for the query and presentation of API data.
- Machine Learning: Machine learning is a field of study concerned with algorithms that learn from examples.
- For my project, I utilized Random Forest and Decision Tree machine learning algorithms to determine which feature(s) is most likely to predict fraud in auto insurance claims. 
- Deployed project via Heroku.

## High Level Findings:

- In terms of Random Forest importances, the highest-ranking feature is 'incident_severity_Major Damage'. Said another way and based on machine learning data, major damage is the most likely feature to be linked to fraud in an automobile insurance claim.

- Both algorithms utilized produced results supporting this finding (Random Forest accuracy of .794 and Decision Tree accuracy of .804). You can think of these measures as the percent of predictions that were correct.

## Users:

- Please refer to config_example.bat file for understanding of required environment variables.

## DON'T FORGET - GitHub:

- GitHub Repository link to your google slide for your recruiter to see what you did on project.

- GitHub Repository should have link to Heroku app if this is still in production and deployed successfully.

- The order is important and keep an eye on final project read me to incorporate the same. Your next goal is to use ML techniques on your existing project and deploy the project again. You can also use Tableau to host the final data and incorporate ML in Tableau before you host on public.tableau.com.

