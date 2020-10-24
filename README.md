# python-challenge
Created a directory for both of the Python Challenges: PyBank and  PyPoll

Inside each directory is the following:
 - A ile called main.py. which is the main script to run for each analysis.
 - A "Resources" folder that contains the CSV files you used. 
 - An "analysis" folder that contains text file that has the results from the analysis.
 
 ## PyBank
 In this challenge, we were tasked with creating a Python script for analyzing the financial records of the company. We were given a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
 
Created a Python script that analyzes the records to calculate each of the following:
 - The total number of months included in the dataset
 - The net total amount of "Profit/Losses" over the entire period
 - The average of the changes in "Profit/Losses" over the entire period
 - The greatest increase in profits (date and amount) over the entire period
 - The greatest decrease in losses (date and amount) over the entire period
 
### Results:
  ```text
Financial Analysis
----------------------------
Total Months:  86
Total:   $38382578
Average Change:   $446309.05
Greatest Increase in Profits:  Feb-2012 ($1170593)
Greatest Decrease in Profits:  Sep-2013 ($-1196225)
   ```
   
   
## PyPoll
In this challenge, we were tasked with helping a small, rural town modernize its vote counting process.  We were given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
 
Created a Python script that analyzes the votes and calculates each of the following:
 - The total number of votes cast
 - A complete list of candidates who received votes
 - The percentage of votes each candidate won
 - The total number of votes each candidate won
 - The winner of the election based on popular vote.
 
### Results:
  ```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
   ```

