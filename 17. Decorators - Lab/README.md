## **01.	Number Increment -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/17.%20Decorators%20-%20Lab/01_number_increment.py)
Having the following code:

        def number_increment(numbers):
            def increase():
                # TODO: Implement
            return increase
            
Complete the code so it works as expected

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|print(number_increment([1, 2, 3]))          |[2, 3, 4]          |




## **02.	Vowel Filter -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/17.%20Decorators%20-%20Lab/02_vowel_filter.py)
Having the following code:

        def vowel_filter(function):
            def wrapper():
                # TODO: Implement
            return wrapper

Complete the code so it works as expected

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@vowel_filter<br>def get_letters():<br>    return ["a", "b", "c", "d", "e"]<br><br>print(get_letters())         |["a", "e"]          |



## **03.	Even Numbers -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/17.%20Decorators%20-%20Lab/03_even_numbers.py)
Having the following code:

        def even_numbers(function):
            def wrapper(numbers):
                # TODO: Implement
            return wrapper

Complete the code so it works as expected

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@even_numbers<br>def get_numbers(numbers):<br>    return numbers<br><br>print(get_numbers([1, 2, 3, 4, 5]))          |[2, 4]          |




## **04.	Multiply -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/17.%20Decorators%20-%20Lab/04_multiply.py)
Having the following code:

        def multiply(times):
            def decorator(function):
                # TODO: Implement
            return decorator
            
Complete the code so it works as expected

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|Complete the code so it works as expected<br>@multiply(3)<br>def add_ten(number):<br>    return number + 10<br><br>print(add_ten(3))         |39         |
|@multiply(5)<br>def add_ten(number):<br>    return number + 10<br><br>print(add_ten(6))          |80 |


