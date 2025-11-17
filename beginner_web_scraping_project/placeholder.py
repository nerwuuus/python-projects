# ============================================================================
# This script downloads all .csv files containing data for 
# every Premier League match during the 2021/2022 season
# ============================================================================
import pandas as pd

# URL structure and parameters
# https://www.football-data.co.uk/mmz4281/2122/E0.csv
root = 'https://www.football-data.co.uk/mmz4281/'
leagues = ['E0', 'E1', 'E2', 'E3', 'EC'] # create a list of leagues: Premier League + lower divisions + Championship

# initialise an empty list to collect intermediate results from the loop
frames = []

# loop through leagues, read multiple .csv, append into a list
for league in leagues:
    df = pd.read_csv(root + '2122' + '/' + league + '.csv', encoding='unicode_escape')
    frames.append(df)

# check the length of frames list. Expected result: 5 (5 files in total)
# len(frames)
