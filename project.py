import sys
import pandas as pd
import numpy as np


def main():
    while True:
        try:
            dataframes = read_csv()
            DF_AIO = pd.concat(dataframes)
            DF_AIO = delete_duplicates_and_sort(DF_AIO)
            DF_AIO = add_prices(DF_AIO)
            make_csv(DF_AIO)

        except ValueError as e:
            if e.args[0] == ('There are negative prices, please check the csv and change these numbers.') or ('Prices cannot be 0, please check the csv and change these numbers.'):
                print(f"Error: {e}")
                sys.exit(1)
            else:
                 print(f"Error: {e}")
                 pass
        except SystemExit:
            print("You has successfully exited the program")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nYou has successfully exited the program")
            sys.exit(1)

# Read the csv(s)
def read_csv():
    dataframes = []
    flag_exit = False
    while True:
        try:
            yes_or_no = input("Do you want to read the default csv? (Yes/No): ").lower()
            if yes_or_no == "yes":
                dataframes.append(pd.read_csv("hammer.csv"))
                dataframes.append(pd.read_csv("nanum.csv"))
                dataframes.append(pd.read_csv("blanco.csv"))  
                return dataframes                 
            if yes_or_no == "no":
                while True:
                    try:
                        csv_name = input("Give me the name of a CSV: ")
                        if csv_name == "exit":
                            raise SystemExit
                        if not csv_name.endswith(".csv"):
                            raise ValueError("The file name is not a .csv.")
                        else:
                            csv_to_add = pd.read_csv(csv_name)
                            dataframes.append(csv_to_add)
                        #answer function
                            flag_exit = answer_function()
                            if flag_exit:
                                break


                    except FileNotFoundError as e:
                        if str(e.filename) == "exit":
                            print("You has successfully exited the program")
                            sys.exit(1)
                        print("Error: The file was not found. Make sure the file name is correct.")
                        pass
                    except ValueError as e:    
                        if e.args[0] == ("The file name is not a .csv."):
                            print(f"Error: {e}")
                            pass
                return dataframes
            if yes_or_no == "exit":
                raise SystemExit
            else: 
                raise ValueError("You must answer yes or no.")
        except ValueError as e:
            if e.args[0] == ("You must answer yes or no."):
                print(f"Error: {e}")
                pass

# Answer
def answer_function():
    i = 0
    while True:
        try:
            answer = input("Do you want to add another csv?: ").lower()            
            if answer == "exit":
                raise SystemExit
            if answer == "yes":
                break
            if answer == "no":
                return True
            if i == 5:
                raise SystemExit
            else:
                i = i+1
                raise ValueError("You must answer yes or no.")
        except ValueError as e:
            print(f"Error: {e}")
            pass

# Remove duplicate rows based on name and watts keep the row with the lowest value in price and sort them
def delete_duplicates_and_sort(DF_AIO):
    DF_AIO = DF_AIO.sort_values("precio").drop_duplicates(subset=["nombre", "watts"], keep="first")
    DF_AIO = DF_AIO.sort_values("watts")
    DF_AIO = DF_AIO.sort_values("nombre").reset_index(drop=True)
    return DF_AIO

#Polinomial regresion function for calculate price with increase
def polynomial_fun():
    x_data = np.array([1,50, 100])
    y_data = np.array([1.4,60,110])
    coefficients = np.polyfit(x_data, y_data, 2)
    polynomial = np.poly1d(coefficients)
    x_data2 = np.array([100,1000])
    y_data2 = np.array([110,1050])
    coefficients2 = np.polyfit(x_data2, y_data2, 1)
    polynomial2 = np.poly1d(coefficients2)
    return polynomial, polynomial2

# Lambda Helper to calculate the price increase with a polynomial regression
def calculate_price_with_increase(precio,polynomial_fun):
    polynomial, polynomial2 = polynomial_fun
    if precio < 0:
        raise ValueError("There are negative prices, please check the csv and change these numbers.")
    if precio == 0:
        raise ValueError("Prices cannot be 0, please check the csv and change these numbers.")
    if 0 < precio <= 100:
        return round((polynomial(precio)), 2)
    if precio > 100:
        return round((polynomial2(precio)), 2)
    else:
        return round(precio * 1.05)
        

# Add two new columns with new prices
def add_prices(DF_AIO):
    DF_AIO["precio_con_aumento"] = DF_AIO["precio"].apply(lambda x: calculate_price_with_increase(x,polynomial_fun()))
    DF_AIO["precio_con_aumento2"] = DF_AIO["precio_con_aumento"].apply(lambda x: calculate_price_with_increase(x,polynomial_fun()))
    return DF_AIO


# Save the result to a new CSV file
def make_csv(DF_AIO):
    DF_AIO.to_csv("AIO.csv", index=False)
    print("The file is ready, check the folder")
    #print(DF_AIO)
    raise SystemExit


if __name__ == "__main__":
    main()