# CSVALL
## Video Demo:  https://youtu.be/TScolN-I9Uw
## Short Description:
This is my final CS50P project
It is a command line program, which grabs n csv files and returns a single csv file with the unique products and adds two new columns of prices calculated with a polynomial regression.
## Long Description:
In my work we have several lists of products from various suppliers and sometimes customers want the cheapest products, but for a person to search through all the lists of suppliers to find the product that the customer wants and compare the price between all of them is a very tedious and time consuming job.
So I created this program consumes several lists of products in csv, it chooses the products with lower prices removing the repeated ones, then it adds a column with a price increase that is calculated through a linear regression resulting in competitive prices in the current market, and then creates a new csv with the result, to make the project I made use of two libraries, pandas to read, manipulate and create the csv, and numpy to make the linear regression with some arbitrarily chosen data.

### Main
To begin with my program starts with the main function and behind it there is a while True loop that will try to do its function and catch any errors that occur and handle them correctly indicating what the failure is.

### dataframe = read_csv
This step what it does is to create a dataframe of all the csv together to be able to work with pandas. 

The function read_csv the first thing it does is to create an empty dataframe that then will fill it with the csv.

Then it creates a variable flag_exit = False that later will be used to exit a nested while loop, it is not a very elegant solution but it was the best that I found to exit nested while loops.

Then starts the first while loop, the first thing we are going to try is to ask the user with an input if he wants to read the default csv or not.

In case of saying "yes" it will read 3 default csv.

In case of saying "exit" it will exit the program, I put this to avoid having to press Ctrl+C to exit the program, which I also handle in the errors in case I want to do it.

In case of not saying yes, no or exit, an error is raised, the user is told to say yes or no, and is asked again.
    
In case of saying "no" it will enter a second while loop where now the user will be asked for the names of the .csv that he wants to read.

in case of saying "exit" it will raise an error and exit the application

in case of writing a file that does not end in .csv it will raise an error, it will tell the user that it is not a .csv and ask him again for a .csv

and in case it doesn't pass the possible errors it will read the csv with pandas and then add it to the dataframes variable.
        
then it will ask the user if he wants to add another csv, I did this in a way that you can add n csv numbers.

the answer goes to another function answer_function(), I did this because it was getting too big and had too many nested loops.
            
In case the user says "exit" it exits the application.
            
In case the user says "yes" a break is made to exit the third while loop and start again the second while loop, where it will ask the user for a csv name.

in case he doesn't answer "yes", "no" or "exit" deneuvo will ask the user for the name of a csv, while it keeps an error counter, when it reaches 5 it exits the application.

In case of saying "no" it returns True to flag_exit leaving the third loop and the second loop at the same time and return the dataframes leaving the first loop.

### DF_AIO = pd.concat(dataframes)
This takes the dataframe data which is a list and converts it into a pandas DataFrame.

### DF_AIO = delete_duplicates_and_sort(DF_AIO)
This does exactly what it says, deletes the duplicates and sorts the DataFrame.

First it sorts the DaraFrame by "price" and deletes the duplicates that have the same "name" and "watts" leaving only the cheapest which is the first one.

Then sort by "name" and "watts" to have an order and return the DataFrame sorted, the index reset was necessary to be able to do the tests.


### DF_AIO = add_prices(DF_AIO)
This function generates two new columns, which are the column "price_with_increase" which is equal to the column "precio" after applying the function "calculate_price_with_increase" and the second one is "price_with_increase2" which is equal to the column "price_with_increase" after applying the function "calculate_price_with_increase".
and the second one is "price_with_increase2" which is equal to the column "price_with_increase" after applying the function "calculate_price_with_increase".

### calculate_price_with_increase(precio)
This function is simple

If the price is negative it raises an error message and warns the user that he has to check the csv.

If the price is zero it raises an error message and warns the user that he has to check the csv.

If the price is between 1 and 100 it multiplies the price by a function that increases the percentage little by little, to find this function it does a polynomial regression with numpy.

If the price is between 101 and 1000 multiply the price by another function that increases the percentage step by step, to smooth that function do a polynomial regression with numpy.

If the price is greater than 1000, multiply by 1.05.

### make_csv(DF_AIO)
To finish this function just save the DataFrame in a csv named AIO.csv and send a message to the user that the file is ready and to check the folder.