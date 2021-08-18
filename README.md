# Rental Calculator for São josé dos Campos

## The problem
- The Problem of anyone who wants to rent an apartment is to analyze and choose a location based on the comparison between price and the  apartment characteristics.

## The project
- To help the users this calculator used [vivareal.com](https://www.vivareal.com.br/), which is a site where anyone can publish and ad to rent their own apartment, so we used the location for São José dos Campos to search apartments and analyze the caracteristics. And for this a Web Scrapping using Selenium was made through the presented process in [data_manipulation_vivareal_selenium.ipynb](https://github.com/tiagotakeshi/rental_calculator/blob/4bcf71fab8f35003c0de5a62bcc42f090e0f047f/data_manipulation_vivareal_selenium.ipynb).
- The data manipulation file also contains part of the process made to transform the data, removing unwanted parts of strings, converting the data, to finally export our final dataset [apto_results_final.csv](https://github.com/tiagotakeshi/rental_calculator/blob/b23b3a9a06cdb08f377e9de6e900c149c9a36243/apto_results_final.csv)
- With the csv file it was possible to make an exploratory data analysis [aed_vivareal.ipynb](https://github.com/tiagotakeshi/rental_calculator/blob/b23b3a9a06cdb08f377e9de6e900c149c9a36243/aed_vivareal.ipynb) which shown us some outliers in price and condominium values, the pattern and correlation between some variables.
- After the EDA, to training the Machine Learning Algorithm, some information was added to the data, to make the calculator more accurated, which was filtering the neighborhood into zones (north, south, east, west and southeast).
- The process of the final data manipulating and the Machine Learning  Algorithm is present in [ml_algorithm.ipynb](https://github.com/tiagotakeshi/rental_calculator/blob/b23b3a9a06cdb08f377e9de6e900c149c9a36243/ml_algorithm.ipynb). There was shown the process made, the training of Random Forest Regressor, the process using GridSearchCV to find the best combination between some parameters, and finally the creation of our regressor.pck (the model trained).
- To make possible to users interectly streamlit was used to create a simple front, and the all the files and the [code](https://github.com/tiagotakeshi/rental_calculator/blob/b23b3a9a06cdb08f377e9de6e900c149c9a36243/calculator.py) is avaiable to be consulted in the [repository](https://github.com/tiagotakeshi/rental_calculator.git).

## Improvements
Some improvements considering a better precision in the results of this project:
- Get more data for a better model trained.
  We used less then 2,000 register
- Analyse each neighborhoob from the scrapping and classify then into one zone (that is a lot of work, beacause it is a hand made process)
- Creating a database with some registers to shown a map with some apartments, near the informed location from users, and theirs characteristcs to the user.
