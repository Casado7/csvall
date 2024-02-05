from project import answer_function, delete_duplicates_and_sort,calculate_price_with_increase, add_prices, make_csv, polynomial_fun
import pytest
import pandas as pd


dataframe_before_delete_duplicates_and_sort = pd.DataFrame({
        'nombre': ['bombillo', 'panel', 'panel', 'bombillo', 'reflector', 'reflector', 'bombillo', 'panel', 'panel', 'bombillo', 'bombillo', 'panel', 'panel', 'bombillo', 'bombillo', 'reflector'],
        'marca': ['hammer', 'hammer', 'hammer', 'hammer', 'hammer', 'hammer', 'nanum', 'nanum', 'nanum', 'nanum', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
        'precio': [1, 2, 3, 2, 60, 100, 1, 2, 3, 1, 1, 2, 3, 2, 3, 20],
        'watts': [8, 10, 20, 9, 500, 1000, 8, 10, 20, 9, 8, 10, 20, 9, 7, 200]
    })
dataframe_after_delete_duplicates_and_sort = pd.DataFrame({
        'nombre': ['bombillo', 'bombillo', 'bombillo', 'panel', 'panel', 'reflector', 'reflector', 'reflector'],
        'marca': ['blanco', 'hammer', 'nanum', 'hammer', 'nanum', 'blanco', 'hammer', 'hammer'],
        'precio': [3, 1, 1, 2, 1, 20, 60, 100],
        'watts': [7, 8, 9, 10, 20, 200, 500, 1000]
    })
data_frame_after_add_prices = {
    'nombre': ['bombillo', 'bombillo', 'bombillo', 'panel', 'panel', 'reflector', 'reflector', 'reflector'],
    'marca': ['blanco', 'hammer', 'nanum', 'hammer', 'nanum', 'blanco', 'hammer', 'hammer'],
    'precio': [3, 1, 1, 2, 1, 20, 60, 100],
    'watts': [7, 8, 9, 10, 20, 200, 500, 1000],
    'precio_con_aumento': [3.9, 1.3, 1.3, 2.6, 1.3, 24.0, 72.0, 110.0],
    'precio_con_aumento2': [5.07, 1.69, 1.69, 3.38, 1.69, 28.80, 86.40, 121.00]
}
input_data = pd.DataFrame({
        'nombre': ['bombillo', 'bombillo', 'bombillo', 'panel', 'panel', 'reflector', 'reflector', 'reflector'],
        'marca': ['blanco', 'hammer', 'nanum', 'hammer', 'nanum', 'blanco', 'hammer', 'hammer'],
        'precio': [3, 1, 1, 2, 1, 20, 60, 100],
        'watts': [7, 8, 9, 10, 20, 200, 500, 1000],
        'precio_con_aumento': [3.9, 1.3, 1.3, 2.6, 1.3, 26.0, 72.0, 110.0],
        'precio_con_aumento2': [5.07, 1.69, 1.69, 3.38, 1.69, 31.20, 86.40, 121.00]})

def test_answer_function():
    assert answer_function("no") == True

def test_answer_function2():
    with pytest.raises(SystemExit):
        answer_function("exit")

def test_answer_function3():
    with pytest.raises(SystemExit):
        answer_function("rere")

def test_answer_function4():
    assert answer_function("yes") == None

def test_delete_duplicates_and_sort():
    assert (delete_duplicates_and_sort(dataframe_before_delete_duplicates_and_sort) == (dataframe_after_delete_duplicates_and_sort)).all

def test_delete_duplicates_and_sort2():
    with pytest.raises(AttributeError):
        delete_duplicates_and_sort(0)

def test_add_prices():
    assert (add_prices(dataframe_after_delete_duplicates_and_sort) == (data_frame_after_add_prices)).all

def test_add_prices2():
    with pytest.raises(TypeError):
        add_prices(0)
    
def test_calculate_price_with_increase():
    with pytest.raises(ValueError):
        calculate_price_with_increase(0,polynomial_fun())

def test_calculate_price_with_increase2():
    with pytest.raises(ValueError):
        calculate_price_with_increase(-1,polynomial_fun())

def test_calculate_price_with_increase3():
    assert calculate_price_with_increase(1,polynomial_fun()) == 1.4

def test_calculate_price_with_increase4():
    assert calculate_price_with_increase(20,polynomial_fun()) == 25.25

def test_calculate_price_with_increase5():
    assert calculate_price_with_increase(90,polynomial_fun()) == 99.03

def test_calculate_price_with_increase6():
    assert calculate_price_with_increase(100,polynomial_fun()) == 110

def test_calculate_price_with_increase5():
    assert calculate_price_with_increase(1000,polynomial_fun()) == 1050

def test_make_csv():
    with pytest.raises(SystemExit):
        make_csv(input_data)

def test_make_csv2():
    with pytest.raises(AttributeError):
        make_csv(0)      