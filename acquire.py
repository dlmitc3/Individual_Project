# #### Individual Project
# 
# ## Predicting Major League Baseball Winning Team Prediction
#
# ### Acquire Major League Baseball Data from baseball-reference.com
# 
# - Data acquired from batting, pitching and fielding game logs for the 2022 MLB season for all 30 teams
# - All logs were combined into one .csv file
# --- When using SR data, please cite us and provide a link and/or a mention. Data source is baseball-reference.com

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import os

#Read local .csv downloaded and combined from 2022 batting logs for all 30 Major League Baseball teams 
#from baseball-reference.com and store data in a dataframe


#Function to get baseball batting log data

def get_MLB_log_data():

    filename = "baseball.csv"


    if os.path.isfile(filename):
       return pd.read_csv(filename)
    else:

        df = pd.read_csv('sportsref_download.csv')
    
        return df
        