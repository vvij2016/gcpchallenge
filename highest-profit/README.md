# Solution for Highest Profit Challenge
Vidushika Vij.  
04/08/2021.  

## Part 1
I used Juptyer notebook with Pandas package to read the data and also filter out rows with non-numeric profit values.   
The Juptyer notebook for the solution is also included in this repository.   

## Part 2
For converting the data to JSON format, I used Pandas in-built function pd.to_json.   
Also, for printing top 20 rows with the highest profit I simply used used the Pandas sort_values function.   
The code for this is included in the Python notebook.   

## Part 3
For analyzing this data using SQL, I loaded the provided dataset into Big Query as a table.   
It successfully loaded the data, but as the column profit contains string values so Big Query loaded this as a string column.   

![](images/picture1)

However, Big Query has functions like CAST to easily convert string columns to numeric values.   
Since, CAST has a strict casting behavior, so instead I used SOFT_CAST function that converts   
the string values into null.   

In real life probably I will convert this column into numeric using a simple transformation and use the resulting table   
and create a new table using the SQL statement as below

![](images/picture2)


