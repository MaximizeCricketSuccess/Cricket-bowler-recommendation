# Cricket-bowler-recommendation
🏏 ML-powered insights for team captains. Analyzing 14 years of ball-by-ball data to enhance decision-making. #CricketAnalytics #IPLPredictions
# Cricket Bowler Recommendation System

## Overview

This repository contains the code and documentation for a Data-Driven Cricket Bowler Recommendation System. The system is designed to predict the number of runs a bowler is likely to concede in the next over of a cricket match, providing valuable insights for team management.

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Example](#example)
- [Future Scopes](#future-scopes)
- [References](#references)

## Introduction

Cricket, a sport celebrated for its strategic complexity, places a significant emphasis on the selection of bowlers during a match. This project aims to develop a recommendation system that suggests the most suitable bowlers for the next over in a cricket match, leveraging mathematical concepts and data analysis techniques.

## Key Features

- **Bowler Performance Prediction:** Predicts the number of runs a bowler is likely to concede in the next over.
- **Data-Driven Decision Making:** Utilizes ball-by-ball data from IPL matches played between 2008 and 2022 for model training.
- **Multiple Linear Regression Model:** Employs a regression model to analyze various performance parameters and make predictions.

## Usage

To use the system, the user needs to input various parameters, including the number of overs bowled, current economy, current strike rate, total wickets taken, boundaries conceded, and dot balls conceded. The system then provides a predicted number of runs the bowler will concede in the next over.

## Dependencies

- Python 3
- pandas
- statsmodels
- numpy

## Example

Enter the number of overs bowled by the bowler till now: 3
Enter current economy of the bowler till the 4th over: 7
Enter current SR of the bowler till the 4th over: 0
Enter current total number of wickets taken by bowler till the 4th over: 0
Enter number of boundaries conceded until now: 1
Enter number of dot balls conceded until now: 4
Predicted Runs: 8.21

## Future Scopes
Match Predictions: Extend predictions to match parameters for platforms like Dream 11.
Video Game Software: Implement the model for cricket video game software.
Bowler-Batsman Combinations: Incorporate batting styles for improved predictions.
Ranking System for Bowlers: Provide a ranked list of bowlers based on wicket maximization and run minimization.

## References
GeeksforGeeks
Dangermouse Cricket - Bowl Strategy
Regression Analysis with Python
