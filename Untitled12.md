# The Relation between Efficiency and Tempreture Degrees
## OM Analytics
***

## Table of Contents
#### Purpose 
#### Discovering and Manulpating the Data
#### Calculating Efficiency
#### Descriptive Statistics
#### Visualizing the Data
#### Conclusion


### Purpose

As an Electrical Engineer had worked for a private company in the Project of Health Facilities Maintenance and Operation. 
He faced a high-temperature problem inside Medical Laboratories and especially in Summer with outside temperatures reach 50 C.
He teamed up with 5 people to solve this problem and was of Business requirements calculating Efficiency for each Temperature Degree. Based on his knowledge in Math, he created a new formula for calculating the Efficiency for Temperature Degrees.

### Discovering and Manipulating the Data

- Importing Libraries
- Reading the Data
- Checking count of Rows and Columns
- Checking types of data for each column
- Rearranging The  Columns
- Renaming the Columns 

### Calculating the Efficiency for each Temperature Degree

- Set Ideal
- Actual and Breakdown 
- Temperature Degrees
- Create a Formula for calculating Actual Efficiency
- Create New Column is called Efficiency
- Creating a new column is called Quality which gives value 'good' if Efficiency greater than or equal 70 otherwise 'bad'.

##### All Temperature Degree in Celsius.

#Ideal Tempreture Degree 
- ideal_temp_deg = 22

#Actual Tempreture Degrees
- actual_temp_deg = lab_df['TemperatureDegree']

#Ideal Efficincy percent
- ideal_eff = 100

#One Temperature Degree Equal 10 percent from Efficiency 
- one_deg = 10

#Actual Efficiency percent
- actual_eff = ideal_eff -(actual_temp_deg -ideal_temp_deg)* one_deg

#Breakdown Tempreture Degree
- Break_temp_deg = ideal_temp_deg + 10

### Descriptive Statistics

- Describing Statistics for Temperature Degree and Efficiency Columns
- The Average, Middle Value, Most Common Value, Minimum and Maximumn values of Temperature Degrees and Efficiency

### Visualizing the Data

![image.png](attachment:image.png)
In the Regional Laboratory, there are **70%** of laboratories assort as _Bad Efficiency_ and **30%** as _Good Efficiency_.
If _Efficiency_ less than **70%** the _Quality_ becomes __Bad otherwise Good__.

#   

![image.png](attachment:image.png)
In Blood Bank , All Rooms assort as Bad Efficiency.

#  

![image.png](attachment:image.png)
In Ploymerase Chain Reaction Laboratory, there are five Rooms assort as Bad Efficiency and one as Good Efficiency.

#  

![image.png](attachment:image.png)
Overall, the Efficiency Rates are decreased with increasing the Temperature Degrees and when a Degree exceeds 25 C the Efficiency Rates are within Bad Rates.

#  

![image.png](attachment:image.png)
The _Blue Graph_ is represented as __Temperature Degree Distribution__ and the _Green Graph_ is represented as __Efficiency Distribution__. Each Temperature Degree is identified with a certain Efficiency Rate. The highest frequency Degrees are in range **27.35 to 29.15** with Efficiency in range **28.50 to 45.00** and the lowest frequency Efficiency in range **22. to 23.95** with Efficiency in range **81.00 to 98.20**.

#  

![image.png](attachment:image.png)
There are 79% of Laboratories assort as Bad Quality and 21% as Good Quality.

#  

![image.png](attachment:image.png)
There are **13** laboratories located in First Floor and **6** laboratories in **Ground Floor**.

#  

### Conclusion

- There is an **inversely relational** between Efficiency rates and Temperature Degrees. 
- Good Efficiency Rates when Temperature Degrees are less than or equal **25 C**. 
- There are **13** laboratories have bad Efficiency Rates and **6** Laboratories have good Efficiency Rates. 
- **68%** of laboratories are located on First Floor and **32%** in Ground Floor. 
- The Temperature Degrees average is about **26.42 C** with Efficiency Rate of **54.24%**, this refers to a Bad Rate.
