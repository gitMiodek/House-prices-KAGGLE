# This repository contains my project predicting house prices based on Kaggle dataset.
The helper README simply describes main steps that I made in order to acomplish the task.
# Main things touched in this project
## Data preprocessing:
- data acquisition
- data visualisation
> I paid attention to findout as much as I could from raw dataset
- handling missing values
> Most of the missing values where acctually informative
- droping obvious outliars
- droping features that have literally no impact on a target prediction
- encoding categorical features
- feature engineering
> Finding features using Mutual Information/PCA
> Finding features manually based on data description
- normalizing data
> Normalizing data is really important as far as result of a prediction model is conserned.
> They work much better when distribution of an input is normally distributed (like Gauss)
## Modeling
After preprocessing of the data i stared working with modeling:
- setup kFold evaluation method
> It is used for cross validation and GridSearchCV
- Choosing five models to predict target(SalePrice)
> Ridge
> RandomForestRegressor
> XGboost
> GradientBoostingRegressor
> SVR
- Finding best hyper-parameters using GridSearchCV
- Fitting models ---> Choosing best one
- Make final prediction.
## Final words
To sum up I would like to mention that while working on this project, I tried to learn as much as I could in terms of 
doing regression project. I tried different techniques within data preprocessing or feature enigneering or even modeling
In next project I will be focused on improving used techniques and test my knowledge as far as classification problem is conserned.

Stay tuned!
