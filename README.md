# Python Challenge
###### by Kurt Pessa

#### Setup
* Created a repository `python-challenge`
* Inside repository, created directories `PyBank` and `PyPoll` for both challenges


## PyBank

#### Setup
* Created a new python file `main.py` that is the main script to run for the analysis
1. Added a `Resources` folder that contains a CSV file `budget_data.csv`
2. Added an `analysis` folder that contains a text file with the results from the analysis

#### Given
* CSV file consisting of two columns:
	1. `Date`
	2. `Profit/Losses`

	![](Images/budget_data.png) 

### Tasks
1. The total number of months included over the entire period

	![](Images/num_months.png)

	![](Images/num_months_output2.png)

2. The net total amount of "Profit/Losses" over the entire period

	![](Images/total.png)

	![](Images/total_output.png)

	* Verified calculation with pandas in a jupyter notebook

	![](Images/sum_pandas.png)

3. The average of the changes in "Profit/Losses" over the entire period

	![](Images/average.png)

	![](Images/average_output.png)
	
	* Verified calculation with pandas
	
	![](Images/average_pandas.png)

4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in losses (date and amount) over the entire period	
	* Set up two variables (lists so I could keep track of both date and value) to track while csvreader is looping through data
	
	![](Images/greatestincrease.png)

	![](Images/output.png)

	* Verified calculation with pandas
	
	![](Images/output_pandas.png)	

	* Looks similar to provided analysis
	
	![](Images/sample_analysis.png)

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

	![](Images/write.png)

	![](Images/file_output.png)