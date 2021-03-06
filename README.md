![mlblogo](https://user-images.githubusercontent.com/102172479/177244878-86154579-aab4-4680-befb-6d8ce1bb0dbe.png)


2021 Major League Baseball (MLB) Prediction and Outcomes

# Executive Summary

## Overview:

The MLB or Major League Baseball, is comprised of 30 teams that play 162 baseball games every year. Official game statistics are kept for every game and have been kept since the mid-1800s. With so much data and statistics, fans and team managers have the opportunity to look back and better understand the game. The understanding and analysis of baseball data can help differentiate the performance of a better performing baseball player or a better performing baseball club.

In this project, I will seek to better understand the game of baseball and try to forecast MLB game outcomes by creating machine learning models. I will create a classification model that will try to predict whether a team will win or lose a game and a linear regresssion model that will try to predict the number of runs in a game using hitting data for games that were already played. lastly I also seek to determine what drivers are indicators of winning.

## Project Goals

- Use MLB baseball data for all 30 teams from the complete 2021 season
F- ind drivers for team wins using baseball data.
- Create a machine learning classification model that predicts team wins
- Find drivers of runs scored
- Create a regression model to predict the number of runs scored in a baseball game

### Conclusion & Key Findings:

I was able to create a machine learning model using classification algorithms to predict whether a team would win or lose a game using a team's previous three games average hitting statistics. I was also able to create a regression model to predict the number of runs a team would have in a game using the team's previous three games average hitting statistics.

- My model was able to predict a baseball games outcome with an accuracy of 58% on out of sample data beating the baseline of 50%.

- My model for predicting the number of runs a baseball team scored also performed better than the baseline accounting for a 35% improvement over the baseline error.

- While not a significant advantage over the baseline, these models may help give a baseball club, a person or group trying their hands at odds.

- The top features used in my model included the 3 game rolling averages per team of:

    - RBIs, runs, hits, homeruns, plate appearances, doubles, walks in a game

- Additional analysis of features used in our model included the 3 game rolling averages per team of previously played games for the following baseball hitting stats:

    - RBIs, hits, plate appearances and home runs

My findings indicate that using past games' hitting performance is not necessarily a signicant predictor of what is going to happen in the next game, but may help you win in gambling.

### Next Steps:

- With more time, I would like to continue trying out other models using new features and changing the hyperparameters to see if we can beat our forecasting performance.
- I would like to incorporate pitching and fielding data to our data set to have more features to predict with and include more seasons of games played.
- I would also like to create a time series model to predict the future record of a team.

## Project Deliverables

- A final report notebook

## Project Context

- I will be using the baseball team hitting game logs data for all 30 MLB team from the 2021 datasets from baseball-reference.com.

- The target variable for this assessment is going to be the feature "is_win" for the classification model and "runs_scored" for the linear regression model.

## DATA DICTIONARY

| Target       | Datatype            | Definition                                                   |
| ------------ | ------------------- | ------------------------------------------------------------ |
| is\_win      | 4858 non-nul: int64 | indicator 0 or 1 for result of game; 0 is a loss, 1 is a win |
| runs\_scored | 4858 non-nul: int64 | number of runs scored in a game                              |


| Feature                  | Datatype              | Definition                                                                       |
| ------------------------ | --------------------- | -------------------------------------------------------------------------------- |
| Team                     | 4858 non-null object  | Name of Major League Baseball Team                                               |
| Date                     | 4858 non-null object  | Date the baseball game was played                                                |
| Opp                      | 4858 non-null object  | Name of the opposing team                                                        |
| Rslt                     | 4858 non-null object  | Result with score of the game                                                    |
| plate\_app               | 4858 non-null int64   | Number of plate appearance                                                       |
| at\_bats                 | 4858 non-null int64   | Number of at bats                                                                |
| runs\_scored             | 4858 non-null int64   | Number of runs scored                                                            |
| hits                     | 4858 non-null int64   | Number of hits                                                                   |
| doubles                  | 4858 non-null int64   | Number of doubles                                                                |
| triples                  | 4858 non-null int64   | Number of triples                                                                |
| HR                       | 4858 non-null int64   | Number of home runs                                                              |
| RBI                      | 4858 non-null int64   | Runs batted in                                                                   |
| bases\_on\_balls         | 4858 non-null int64   | Bases on balls; walks                                                            |
| intentional\_bb          | 4858 non-null int64   | Intentional walks                                                                |
| strikeouts               | 4858 non-null int64   | Number of strikeouts                                                             |
| hit\_by\_pitch           | 4858 non-null int64   | Number of times hit by pitch                                                     |
| sac\_hits                | 4858 non-null int64   | Sacrifice hits                                                                   |
| sac\_flies               | 4858 non-null int64   | Sacrifice fly balls                                                              |
| reached\_on\_error       | 4858 non-null int64   | Bases reached on error                                                           |
| double\_plays            | 4858 non-null int64   | Number of double plays                                                           |
| stolen\_bases            | 4858 non-null int64   | Number of stolen bases                                                           |
| caught\_stealing         | 4858 non-null int64   | Number of times caught stealing a base                                           |
| batting\_avg             | 4858 non-null float64 | Batting average                                                                  |
| OBP                      | 4858 non-null float64 | On base percentage                                                               |
| SLG                      | 4858 non-null float64 | Slugging percentage; (Hits+(2Doubles)+(3Triples)+(4\*Homeruns)/Number of at bats |
| OPS                      | 4858 non-null float64 | OBP + SLG                                                                        |
| left\_on\_base           | 4858 non-null int64   | Number of players left on base                                                   |
| num\_players\_used       | 4858 non-null int64   | Number of players used in a game                                                 |
| handedness\_opp\_pitcher | 4858 non-null object  | Opposing pitcher handedness, left or right                                       |
| Opp. Starter (GmeSc)     | 4858 non-null object  | Name of opposing pitcher                                                         |
| is\_away                 | 4858 non-null int64   | Indicator whether game was away; 0 was not away, 1 was away                      |
| is\_win                  | 4858 non-null int64   | Indicator whether game was won; 0 was lost, 1 was won                            |
| made\_playoffs           | 4858 non-null int64   | Indicator whether team made playoffs; 0 not made playoffs, 1 did make playoffs   |

# DATA SCIENCE PIPELINE

## PLAN:

### PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

See my Trello board here --> https://trello.com/b/6DTs1uWA/individual-projects

- I will acquire data from baseball-reference.com. 
- I will download all 30 MLB teams' baseball hitting game logs and combine them into one .csv file. 
- I will prepare the data using a prepare.py file which will get rid of unneeded columns,rename columns, and create new columns to capture rolling averages and encode columns. 
- I will explore the data by looking for possible relationships between features and look at how they are distributed by creating plots and looking at the data. 
- I will create models using Decision Tree, Random Forest and K - Nearest Neighbors Classifiers. 
- I will then compare the models that were run on training data to validate data before running our model on the test data to get the final accuracy. 
- I will then create linear regression models using Linear Regressor, Tweedie Regressor, Lasso Lars Regressors, and Polynomial Linear Regressors, evaluate model performance and then run the best model on out of sample data. 
- I will then create and turn in a final Jupyter Notebook with the code of this entire process.

## ACQUIRE:

### Plan -> ACQUIRE -> Prepare -> Explore -> Model & Evaluate -> Deliver

## Obtain Major League Baseball Data from baseball-reference.com

- All data is acquired from batting game logs for all 30 Major League Baseball teams for the year 2021
- Baseball data was exported into an Excel file from the website for each baseball team
- All batting logs were then combined into one .csv file
- Data source is baseball-reference.com

## PREPARE:

### Plan -> Acquire -> PREPARE -> Explore -> Model & Evaluate -> Deliver

I prepped and cleaned the data acquired from baseball-reference.com. I then used functions in prepare.py to accomplish the following:

- Create 3 game rolling average columns for all hitting stats for use in predictive modeling
- Create 'is_away' column to capture that the game was played away, not at home stadium Renamed columns for easier readability
- Create 'is_win' column to capture the result of the game, win or loss
- Create 'made_playoffs' to capture whether the team made it to the playoffs
- Create function, prepare_data(), to clean up and prepare all data acquired as described above
- Create dummy variables for categorical features

## EXPLORE:

### Plan -> Acquire -> Prepare -> EXPLORE -> Model & Evaluate -> Deliver

I visualized combinations of variables to compare relationships and check for independence or correlation between variables.

For the classification model predicting whether the team won, I ran statistical tests for independence for the following questions:

### Hypothesis 1: Is winning related to number of runs scored?

H0: There is no difference between number of runs scored in a winning game and the overall average.

Ha : There is a difference between number of runs scored in a winning game and the overall average.

FINDING: We rejected the hypothesis that winning is not related to number of runs scored

### Hypothesis 2: Does number of hits differ by winning teams?

H0 : There is no difference between number of hits by winning teams and the overall average.

Ha: There is a difference between number of hits by winning teams and the overall average.

FINDING: We rejected the hypothesis that winning is not related to number of hits in a game

### Hypothesis 3: Does number of home runs differ by winning teams?

H0 : There is no difference between number of home runs by winning teams and the overall average.

Ha : There is a difference between number of home runs by winning teams and the overall average.

FINDING: We rejected the hypothesis that winning is not related to number of homeruns in a game

### Hypothesis 4: Is winning related to the number of runs batted in (RBI)?

H0 : There is no difference between number of runs batted in in a winning game and the overall average.

Ha: There is a difference between number of runs batted in in a winning game and the overall average.

FINDING: We rejected the hypothesis that winning is not related to number of runs batted in a game

### Hypothesis 5: Is winning related to the number of total appearances at the plate by a player in the game?

H0 : There is no relationship between winning and the number of plate appearances.

Ha: There is a relationship between winning and the number of plate appearances.

FINDING: We rejected the hypothesis that winning is not related to number of total plate appearances in a game

### Hypothesis 6: Is winning related to the number of doubles that were hit in the game?

H0 : There is no relationship between winning and the number of doubles in a game.

Ha: There is a relationship between winning and the number of doubles in a game.

FINDING: We rejected the hypothesis that winning is not related to number of doubles hit in a game

### Hypothesis 7: Is winning related to the number of bases that were obtained by being walked by the pitcher?

H0 : There is no relationship between winning and the number of walks in a game.

Ha: There is a relationship between winning and the number of walks in a game.

FINDING: We rejected the hypothesis that winning is not related to number of walks in a game

### Hypothesis 8: Is winning related to whether the team is playing away?

H0 : There is no relationship between winning and a team playing away.

Ha: There is a relationship between winning and a team playing away.

FINDING: We rejected the hypothesis that winning is independent of whether a team is playing away

For the linear regression models predicting the number of runs scored, I ran statistical tests for independence.

## MODEL:

### Plan -> Acquire -> Prepare -> Explore -> MODEL -> Deliver

The goal is to develop a classification and regression model that performs better than the baseline.

**For the classification model predicting whether a team would win or lose, I chose the Random Forest model because of its highest accuracy in both train and validate with low overfitting.**

- Random Forest Model had an accuracy of 58% using out of sample data

- This was higher than the baseline accuracy of 50%

- Features used for this model included 3 game rolling averages for:

    - 'roll_runs_scored' - runs scored
    - 'roll_RBI' - RBI
    - 'roll_hits' - hits per game
    - 'roll_HR' - homeruns
    - 'roll_plate_app' - total plate appearances
    - 'roll_doubles' - doubles
    - 'roll_bases_on_balls' - walks or bases on balls

**For linear regression model predicting number of runs, I chose the Ordinary Least Squares Linear Regression model due to its lowest RMSE and highest explained variance, 
R
2**

- The Linear Regression model performed well on out of sample (test) data beating the baseline with an explained variance score, 
R
2
, of 35% and came up with the lowest RMSE of 2.43.
- Features used for this model include rolling averages for the following baseball hitting stats:
    - 'roll_RBI' - runs batted in; a stat indicating that a baseball player got a hit that resulted in a run being scored.
    - 'roll_hits' - rolling average of hits in the past 3 games per team
    - 'roll_plate_app' - rolling average of plate appearances in the past 3 games per team
    - 'roll_HR' - rolling average of home runs in the past 3 games per team

## DELIVER:

### Plan -> Acquire -> Prepare -> Explore -> Model -> DELIVER

- The final product will be a Github repository containing your work with any .py files required to acquire and prepare the data and a clearly labeled final Jupyter Notebook that walks through the pipeline.

## HOW TO RECREATE THIS PROJECT:

To recreate this project you will need the following files from this repository:

- README.md
- acquire.py
- prepare.py
- explore.py
- Final_Baseball_Project_Notebook.ipynb
- .csv file from baseball-reference.com

