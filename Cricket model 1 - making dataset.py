import numpy as np
import pandas as pd

# reading match data on previous IPL matches (2008 - 2022)
matches = pd.read_csv("/Users/sakarth/Downloads/IPL_Matches_2008_2022.csv")
# reading ball-by-ball data for the above the retrieved matches
ballbyball = pd.read_csv("/Users/sakarth/Downloads/IPL_Ball_by_Ball_2008_2022.csv")

# Create a DataFrame with unique bowlers
unique_bowlers = pd.DataFrame(pd.unique(ballbyball['bowler']), columns=['bowler'])

"""
input:
bowler details: economy, strike rate, wickets taken, runs conceded, and dot balls
(till the current_over)

calculating CUMULATIVE data from the over data for the entered bowlers.

run a linear regression model for the parameters we asked as input and which we computed.
"""
no_bowlers = len(unique_bowlers['bowler'])
print(unique_bowlers)
print(type(ballbyball['total_run'][0]))
# parsing and processing data over by over for the 6 parameters
for over in range(0, 20):
    unique_bowlers[f'economy_{over}'] = np.zeros(no_bowlers)
    unique_bowlers[f'SR_{over}'] = np.zeros(no_bowlers)
    unique_bowlers[f'wickets_{over}'] = np.zeros(no_bowlers)
    unique_bowlers[f'runs_{over}'] = np.zeros(no_bowlers)
    unique_bowlers[f'dot_{over}'] = np.zeros(no_bowlers)
    unique_bowlers[f'boundary_{over}'] = np.zeros(no_bowlers)

    """computing the parameters till the ith over for the last 14 years from our ball_by_ball data."""

    for bowler in range(0, len(unique_bowlers)):

        runs = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler])]["total_run"].sum()
        legal_balls = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler]) & (ballbyball['ballnumber'] <= 6)]["ballnumber"].count()
        wickets = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler])]["isWicketDelivery"].sum()
        dots = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler]) & (ballbyball['total_run'] == 0)]["isWicketDelivery"].count()
        boundaries = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler]) & ((ballbyball['total_run'] == 4) | ((ballbyball['total_run'] == 6)))]['total_run'].count()
        matches = ballbyball[(ballbyball['overs'] <= over) & (ballbyball['bowler'] == unique_bowlers['bowler'].loc[bowler])]['ID'].unique()
        matches = len(matches)
        economy = (runs / legal_balls)*6 if legal_balls > 0 else 0  # Avoid division by zero
        SR = runs/wickets if wickets > 0 else 0
        dot_avg = dots/matches if matches > 0 else 0
        boundaries_avg = boundaries/matches if matches > 0 else 0
        runs = runs/matches if matches > 0 else 0
        wickets = wickets/matches if matches > 0 else 0

        unique_bowlers.at[bowler, f'economy_{over}'] = round(economy , 2)
        unique_bowlers.at[bowler, f'SR_{over}'] = round(SR ,2)
        unique_bowlers.at[bowler, f'wickets_{over}'] = round(wickets, 2)
        unique_bowlers.at[bowler, f'runs_{over}'] = round(runs, 2)
        unique_bowlers.at[bowler, f'dot_{over}'] = round(dot_avg, 2)
        unique_bowlers.at[bowler, f'boundary_{over}'] = round(boundaries_avg, 2)


print(unique_bowlers)
unique_bowlers.to_csv("/Users/sakarth/Downloads/unique_bowlers_data.csv")