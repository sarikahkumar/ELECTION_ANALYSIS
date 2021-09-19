# **ELECTION ANALYSIS**
---
## **Overview of Project**

This is an an analysis of the recent congressional elections held in Colorado

---
### **Purpose**

The purpose of this analysis is to provide a report to Colorado Board of Elections based on the recent congressional election as requested by a Board employee. The following information is provided in the report:

- Total number of votes cast
   
- A complete list of candidates who received votes
   
- Total number of votes each candidate received
   
- Percentage of votes each candidate won
   
- The winner of the election based on popular vote
   
- The list of counties in the election
    
- The voter turnout of each county
   
- The percentage of votes from each county 
   	
- The county with the highest turnout

## **Resources**

- Data source: election_results.csv. _This csv file is available in the Resources folder of this repository_

- Software : Python 3.7.6, Visual Studio Code 
	
## **Election Audit Results**

![election_results file](https://user-images.githubusercontent.com/89427676/133938175-11f7e555-0893-46b2-b8e8-cbeb5798fff6.png)
_The results of the election has been written to a text file named election_results.txt by the program. The code used to generate results is saved in this repository as PyPoll_rChallenge_starte_code.py, and the output file is saved in the analysis folder of this repository_

As seen above, 

- The total number of votes cast in the election is 369,711

- There were 3 candidates, 

  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- 3 counties participated in the election,

  - Jefferson
  - Denver
  - Arapahoe

- The total votes cast in each county and percentage of votes is given below:

  - Jefferson county registered 10.5% of total votes with 38,855 votes
  - Denver county registered 82.8% of total votes with 306,055 votes
  - Arapahoe county registered 6.7% of total votes with 24,801 votes

- Denver county registered the maximum polls

- The candidate results in the election is given below:
  - Charles Casper Stockham got 23.0% votes with 85,213 votes
  - Diana DeGette Stockham got 82.8% votes with 306,055 votes
  - Raymon Anthony Doane Stockham got 6.7% votes with 24,801 votes

- The winner of the election was **Diana DeGette Stockham** with **82.8%** votes and **306,055** votes
---
### **Election Audit Summary**

The code used in this program can be used for any election results analysis, if the source file format is similar to the _election_results.csv_ file in which third column contains candidate name and second column contains county name. However, if election analysis needs to be done incorporating more data elements given in source file, modifications can be made in the code while retrieving respective data from source file columns. For example, if there is a column mentioning political party, code can be modified to retrieve the winning party name as follows:

- Declare a variable before 'with open' to hold political party name
	
- Within the for loop retrieve the political party name from each row and assign it to a variable (Same way we retrieved candidate name)
	
- Follow similar procedure as we did for getting individual candidate names, vote percentages, number of votes, to determine and print the winning party statistics
	
