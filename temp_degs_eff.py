"""
Created on Fri Sep  4 21:08:12 2020

@author: Abdulaziz Alsulami

This program asks the user to enter a list for Temperature Degrees as inputs, 
then calculates the Efficiency Rate for each Temperature Degree and assesses 
each Degree according to its Rate as Good or Bad. After that, it displays some 
statistical information such as count, mean, standard deviation, menimum, 
and maximum values. Finally, it shows some graphs that appear the relation between 
the independent variable 'Temperature Degree' and  the dependent variable 
'Efficiency Rate', and how much the percent of Bad and Good Rates.

"""


# import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create TemperatureDegreeEfficiency class
class TemperatureDegreeEfficiency:
    
    def __init__ (self, temp_deg=[]):
        
        """
        Accept one argument as a list of temperature degrees 
        and store it as a list in a variable is called actual_temp.
        
        """
        
        # store temperature degrees in actual_temp
        self.actual_temp = temp_deg
        
    def _calculating_efficiency(self, id_temp=22, id_eff=100, one_temp=10):
        
        """
        Accept three arguments 
        id_temp refers to an ideal temperature 
        id_eff refers to an ideal efficiency 
        one_temp refers to that each temperature degree is equalied to 10 percent of efficiency
        then calculates actual efficiency and store it as a list in a variable is called actual_eff.
        
        """
        # store ideal temperature degree in ideal_temp
        self.ideal_temp = id_temp
        
        # store ideal efficiency rates in ideal_eff
        self.ideal_eff = id_eff
        
        # store one_temp '10' in one_temp_ten_eff
        self.one_temp_ten_eff = one_temp
        
        # set actual_eff with an empty list
        self.actual_eff = []
        
        # create formula inside the loop for calculating efficiency rate 
        # for each temperature degree and store it in actual_eff variable
        for temp in self.actual_temp:
            self.formula = self.ideal_eff - \
                            (temp - self.ideal_temp) * self.one_temp_ten_eff
            self.actual_eff.append(round(self.formula,2))
        
        # return to actual_eff
        return self.actual_eff
  
    def _calculating_quality(self):
        
        """
        Assesses each an efficiency rate if it greater than 70 sorts as Good
        and if it less than 70 sorts as Bad then stor them as a list in a variable is called quality.
        
        """
        # filter variable with None value
        self.filter = None
        
        # quality variable with empty list
        self.quality = []
        
        # assess each an efficiency rate if it greater than 70 sort it as Good
        # otherwise as Bad then store them in quality variable
        for eff in self.actual_eff:
            if eff >= 70:
                self.filter = 'Good'
            else:
                self.filter = 'Bad'
                
            # store them in quality variable    
            self.quality.append(self.filter)
        
        # return quality variable
        return self.quality
    
    def _data_frame(self):
        
        """
        create a variable as a dictionary is called data with three keys and values 
        first key is called Temperature_Degree consistes list of actual temperature degrees
        second key is called Efficiency_Rate contents list of actual efficiency Rates
        third key is called Quality contents list of Quality type 
        then frames this data and store it as a framed data in a variable is called dataset.
        
        """
        # data variable with three lists as values and three keys
        data = {
                'Temperature_Degree': self.actual_temp, 
                'Efficiency_Rate': self.actual_eff, 
                'Quality': self.quality
                }
        
        # Create data frame for data variable and store it in dataset variabel
        dataset = pd.DataFrame(data, index= np.arange(len(self.actual_temp)))
        self.dataset = dataset
        
        # return dataset variable
        return self.dataset
    
    # def _display_(self):
    #     self._good_qul
    #     self._bad_qul
    #     print(self._good_qul, '\n')
    #     print(self._bad_qul, '\n')
    
    def _good_quality(self):
        
        """
        Filtring dataset according to Good quality  
        """
        
        good = self.dataset[self.dataset.Quality == 'Good']
        txt = 'There are {0} Degrees have Good Quality: '.format(len(good))
        print(txt, end='\n')
        return good
    
    def _bad_quality(self):
        
        """
        Filtring dataset according to Bad quality  
        """
        bad = self.dataset[self.dataset.Quality == 'Bad']
        txt = 'There are {0} Degrees have Good Quality: '.format(len(bad))
        print(txt, end='\n')
        return bad
    
    def _statistics(self):
        
        """
        Display statistics for a dataset 
        
        """
        self.desc = self.dataset.describe()
        return self.desc
    
    def _visulizing_temperature_efficiency(self):
        
        """
        Create a line plot graph that shows the relation between independent variable
        'Temperature_Degree' and dependent variable 'Efficiency_Rate'
        
        """
        plt.figure(figsize=(15,5))
        
        X = self.dataset['Temperature_Degree']
        Y = self.dataset['Efficiency_Rate']
        
        sns.pointplot(
                    data=self.dataset.copy(),
                    x=X, 
                    y=Y, 
                    hue='Quality',
                    scale=0.6, 
                    color='b', 
                    palette=['red','blue']
                     )

        plt.title('Efficiency vs Temperature Degrees', fontsize=15)
        plt.xlabel('Temperature Degrees', fontsize=15)
        plt.ylabel('Efficiency', fontsize=15)

        plt.legend(loc= 1, fontsize='small')
        plt.grid(True)
        plt.show()
    
    def _visulizing_quality(self):
        
        """
        Creatae bar plot graph that shows number of Good and Bad quality 
        
        """
        quality_percent = self.dataset['Quality'].value_counts(normalize=True)
        quality_percent
        
        plt.figure(figsize=(8,5))
        plt.axis([0,2,0,0.85])

        X = quality_percent.index
        Y = quality_percent
        sns.barplot(X, Y, alpha=0.6,palette=['red','blue'])

        plt.title('Quality Rate', fontsize=15)
        plt.xlabel('Quality', fontsize=15)
        plt.ylabel('Rate', fontsize=15)
        
        plt.grid(True)
        plt.show()




def evaluate_input():
    
    """
    Order from user to enter a list of temperature degrees n the range from 22 to 32 seperated with ','
    then evaluated if it pass conditions return to user's input otherwise display message and return first line of loop. 
    """
    temp_deg = []
    obj = None
    instruction = '''Enter LIST of temperature degrees seprating by commam ',' in the range from 22 to 32 such as [ 22.5, 26 ] or type < temp_degs > for run programm with default temperature degrees or type < 0 > for exit'''
    message = '''< {0} > is not valid. Should enter list of integer or float numbers seperate by comma ',' in range 22 to 32'''
    print(instruction)
    cond = True
    
    temp_degs = [
                28.3, 27.55, 28.42, 26.81, 25.6, 28.07, 28.24, 29.15,
                28.29, 27.65, 24.35, 26.93, 27.04, 26.06, 23.12, 26.06,
                22.18, 24.78, 26.34
                ]   
    
    while cond:
        # take temperature degrees from user as inputs
        user = input('>>> ')
        # if user equal 0 go out 
        if user == '0':
            break
        
        # try user values
        try:
            # evaluate user inputs by remove all comma ',' 
            # and remaine all numbers and store them in obj variable
            obj = eval(user)
            
            # accept each number if it is integer or float 
            # and greater than or equal 22 and less than or equal 32
            for number in obj:
                if (type(number) is int or type(number) is float) and int(number) >=22 and int(number)<=32:
                    
                    # store number in temp_deg list
                    temp_deg.append(number)
                
                # if not raise exception 
                else:
                    raise
                # if index of obj at the last value go out from while loop
                if number == obj[-1]:
                    cond = False
        # print message for user and come back to first line ' user variable'
        except:
            print(message.format(user))
    
    # return temp_deg if not empty otherwise empty string
    return temp_deg if temp_deg != [] else ''





def run_program():
    # call evaluate_input function and store its value in lst_temp_degs variable
    lst_temp_degs = evaluate_input()
    
    if lst_temp_degs == '':
        return leave_comment()

    # call class TemperatureDegreeEfficiency and store it in reglab variable
    reglab = TemperatureDegreeEfficiency(lst_temp_degs)
    
    
    # Personal_functins = [func for func in dir(reglab) 
    #                       if '__' not in func and '_' in func[0]]
    
    print('List of Temperature Degrees: ', reglab.actual_temp, sep= '\n', end='\n\n')

    while True:
        
        #ask user if he want to calculate Efficiency rate type 1 or 0 for exit
        message = 'Do you want to calculate the Efficiency rate for each Temperature Degree. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 calculate Efficiency rate then break the loop
        if user == '1':
            print('List of Efficiency Rates: ', reglab._calculating_efficiency(), sep='\n', end='\n\n')
            break
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
       
        
    while True:
        
        #ask user if he want to calculate Quality types type 1 or 0 for exit
        message = 'Do you want to calculate the Quality Types for each Temperature Degree. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 calculate Quality type then break the loop
        if user == '1':
            print('List of Quality Types: ', reglab._calculating_quality(), sep='\n', end='\n\n')
            break 
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop       
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
                
    while True:
        
        #ask user if he want to calculate Quality types type 1 or 0 for exit
        message = 'Do you want to see all data as a table. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 create data frame for Temperature Degrees, Efficiency Rates and Quality Types then break the loop
        if user == '1':
            print('Data Frame for Temperature Degrees, Efficiency Rates and Quality Types: ', reglab._data_frame(), sep='\n', end='\n\n')
            break
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop 
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
         
    while True:
        
        #ask user if he want to see Good Efficiency Rates type 1 or 0 for exit
        message = 'Do you want to see Good Efficiency Rates. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 make filter for a data frame to display Good Efficiency Rates then break the loop
        if user == '1':
            print(reglab._good_quality(), end='\n\n')
            break
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop 
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
             
    while True:
        
        #ask user if he want to see Bad Efficiency Rates type 1 or 0 for exit
        message = 'Do you want to see Bad Efficiency Rates. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 make filter for a data frame to display Bad Efficiency Rates then break the loop
        if user == '1':
            print(reglab._bad_quality(), end='\n\n')
            break
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop        
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
    
    while True:
        
        # ask user if he want to see some Statistics type 1 or 0 for exit
        message = 'Do you want to see some Statistics. Type < 1 > for continue or < 0 > for exit'
        print(message, '\n')
        user = input('>>> ')
        
        # if user type 1 display some statistics then break the loop
        if user == '1':
            print('Some Statistics: ', reglab._statistics(), sep='\n', end='\n\n')
            break
        
        # if user type 0 or space return to leav_comment function for exit
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop        
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
             
    while True:
        
        # print messages and graphs as instructions and aks user for type a number of graph 
        message = 'Do you want to see some graphs.'
        message1 = 'Type the graph number that you would like to see or < all > for all graphs or < 0 > for exit'
        print(message, message1, sep='\n\n', end='\n\n')

        graph1 = 'Relation between Temperature Degrees and Efficiency Rates: 1'
        graph2 = 'Good and Bad Quality Destribution: 2'
        print(graph1, graph2, sep='\n')
        
        user = input('>>> ')
        
        # if user type 2 display graph2
        if user == '1':
            g1 = reglab._visulizing_temperature_efficiency()
        
        # if user type 3 display graph3 and return first line of the loop
        elif user == '2':
            g2 = reglab._visulizing_quality()
            
        # if user type all display all graphs and return leave_comment function
        elif user == 'All'.lower():
            g1 = reglab._visulizing_temperature_efficiency()
            g1 = reglab._visulizing_quality()
            return leave_comment()

        # if user type 0 or space return leave_comment function
        elif user == '0' or user =='':
            return leave_comment()
        
        # otherwise print error and return first line of the loop        
        else:
            print('Invalid value { 0 }'.format(user))
            print(message)
        
def leave_comment():
    
    # ask user to leave a comment or type 0 for exit
    message = 'Before exit, Leave a comment or type < 0 > for exit: '
    user = input(message)

    comment = user
    
    # return message
    message = 'Thank you for your use of the program.'
    return message

if __name__ == '__main__':
    run_program()





































