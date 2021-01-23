# The Relationship between Efficiency and Temperature Degrees 
## O&M Analytics 


### Table of Contents 
- Introduction
- Target
- Discovering and Manipulating the Data Calculating Efficiency
- Descriptive Statistics
- Visualizing the Data
- Conclusion 
- Note


### Introduction 
As an Electrical Engineer had worked for a private company in the Project of Health Facilities 'O&M' aka Operation and Maintenance. He faced a high-temperature problem inside Medical Laboratories and especially in Summer with outside temperatures reach 50 C. He teamed up with 5 people to solve this problem and was of Business requirements, calculating Efficiency for each Temperature Degree. Based on his knowledge in Math, he created a new formula to calculate the Efficiency of Temperature Degrees which based on it can measuring quality. 


### Target 
Calculating Efficiency of the Internal Temperature Degrees for Medical Laboratories in The Regional Laboratory and Central Blood Bank. Finding a Relationship between Temperature Degrees as 'Independent Variable', Efficiency Rates and Quality as 'Dependent Variable'. 


### Discovering and Manipulating the Data 
- Importing Libraries
- Reading the Data
- Checking count of Rows and Columns Checking types of data for each
- column Rearranging The Columns
- Renaming the Columns 


### Calculating the Efficiency for each Temperature Degree 
- Set Ideal, Actual and Breakdown Temperature Degrees
- Create a Formula for calculating Actual Efficiency
- Create new column is called Efficiency
- Create a new column is called Quality which gives value 'good' if Efficiency greater than or equal 70 otherwise 'bad'. 


### All Temperature Degree in Celsius. 
- Ideal Temperature Degree 
    `Ideal_deg = 22 C` 
- Actual Temperature Degrees 
    `Actual_deg = [28.3, 27.55, 28.42, 26.81, 25.6 , 28.07, 28.24, 29.15,28.29,27.65, 24.35, 26.93, 27.04, 26.06, 23.12, 26.06, 22.18, 24.78, 26.34]`
- Ideal Efficiency rate
    `deal_eff = 100 %` 
- One Temperature Degree Equates 10 percent from Efficiency 
    `one_deg = 10 %` 
- Actual Efficiency percent
    $actual_eff = ideal_eff - (actual_temp_deg -ideal_temp_deg) * one_deg$
- Breakdown Temperatur Degree
    `Break_temp_deg = ideal_temp_deg + 10 = 22 + 10 = 32 C`


### Descriptive Statistics 
Describing Statistics for Categorical and Numerical Columns. The Average, Middle Value, Most Common Value, Minimum and Maximum values of Temperature Degrees and Efficiency 


### Visualizing the Data 
- In the Regional Laboratory, there were **70% of laboratories assort as Bad Efficiency and 30% as Good Efficiency**. If an Efficiency less than **70%**, the Quality becomes **Bad otherwise Good**. 
- In Blood Bank, All Rooms assort as Bad Efficiency. 
- In Ploymerase Chain Reaction Laboratory, there were **five Rooms** assort as Bad Efficiency and **one** as Good Efficiency. 
- Overall, the Efficiency Rates were decreased with increasing the Temperature Degrees and when a Degree exceeded **25 C** the Efficiency Rates were within Bad Rates. 
- The highest frequency Degrees were in range **27.35 to 29.15** with Efficiency in range **28.50 to 45.00** while the lowest frequency Efficiency were in range **22.00 to 23.95** with Efficiency in range **81.00 to 98.20**. 
- There are **79%** of Laboratories assort as Bad Quality and **21%** as Good Quality. 
- There are **13 laboratories** located in First Floor and **6 laboratories** in Ground Floor.


### Conclusion 
- There is an **inversely relational** between Efficiency rates and Temperature Degrees.
- Good Efficiency Rates when Temperature Degrees are less than or equal **25 C**.
- There are **13 laboratories** have bad Efficiency Rates and **6 Laboratories** have good Efficiency Rates.
- **68%** of laboratories are located on First Floor and **32%** in Ground Floor.
- The Temperature Degrees average is about **26.42 C** with Efficiency Rate of **54.24%**, this refers to a Bad Rate. 


### Note
There are two files in this reposity
- Jupyter Notebook: step by step for all information I mentioned up
- Python Script: you can run this script then it will interactes with you and appear some instruction to giude you and get the information.
