## **01.	Custom Range -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/01_custom_range.py)
Create a class called custom_range that receives start and end upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|one_to_ten = custom_range(1, 10)<br>for num in one_to_ten:<br>       print(num)        |1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10          |




## **02.	Reverse Iter -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/02_reverse_iter.py)
Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|reversed_list = reverse_iter([1, 2, 3, 4])<br>for item in reversed_list:<br>       print(item)          |4<br>3<br>2<br>1          |



## **03.	Vowels -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/03_vowels.py)
Create a class called vowels which should receive a stirng. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|my_string = vowels('Abcedifuty0o')<br>for char in my_string:<br>       print(char)    |A<br>e<br>i<br>u<br>y<br>o          |




## **04.	Squares -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/04_squares.py)
Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|print(list(squares(5)))          |[1, 4, 9, 16, 25]          |



## **05.	Generator Range -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/05_generator_range.py)
Create a generator function called genrange that receives a start and an end. It should generate all the numbers from the start to the end (inclusive).

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|print(list(genrange(1, 10)))         |[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]        |



## **06.	Reverse string -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/15.%20Iterators%20and%20Generators%20-%20Lab/06_reverse_string.py)
Create a generator function called reverse_text that receives a string and yield all string characters in reversed order.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|for char in reverse_text("step"):<br>        print(char, end='')          |pets          |



