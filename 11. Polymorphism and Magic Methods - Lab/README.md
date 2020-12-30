## **01.	Execute -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/11.%20Polymorphism%20and%20Magic%20Methods%20-%20Lab/01_execute.py)
Create a function called execute that receives a function as first argument and then all the other arguments.  
Return the result of the execution of the passed function with that arguments.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|def say_hello(name, my_name):<br><pre>    print(f"Hello, {name}, I am {my_name}")</pre><br><br>def say_bye(name):<br><pre>    print(f"Bye, {name}")</pre><br><br><br>execute(say_hello, "Peter", "George")<br>execute(say_bye, "Peter")   |Hello, Peter, I am George<br>Bye, Peter          |




## **02.	Instruments -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/11.%20Polymorphism%20and%20Magic%20Methods%20-%20Lab/02_instruments.py)
Create a function called play_instrument which will receive an instance of an instrument and will print it's play() method.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|class Guitar:<br><pre>    def play(self):</pre><br><pre>        print("playing the guitar")</pre><br><br>guitar = Guitar()<br>play_instrument(guitar)        |playing the guitar          |
|class Piano:<br><pre>    def play(self):</pre><br><pre>        print("playing the piano")</pre><br><br>piano = Piano()<br>play_instrument(piano) |playing the piano |



## **03.	Shapes -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/11.%20Polymorphism%20and%20Magic%20Methods%20-%20Lab/03_shapes.py)
Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter.  
Create classes Circle (receives radius upon initialization) and Rectangle (receives height and width upon initialization) that implement those methods (returning the result).  
The fields of Circle and Rectangle should be private.  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|circle = Circle(5)<br>print(circle.calculate_area())<br>print(circle.calculate_perimeter())          |78.53981633974483<br>31.41592653589793          |
|rectangle = Rectangle(10, 20)<br>print(rectangle.calculate_area())<br>print(rectangle.calculate_perimeter()) |200<br>60 |




## **04.	ImageArea -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/11.%20Polymorphism%20and%20Magic%20Methods%20-%20Lab/04_image_area.py)
Create a class called ImageArea which will store the width and the height of an image. Create a method called get_area() which will return the area of the image. We have to also implement all the magic methods for comparison of two image areas (>, >=, <, <=, ==, !=) which will compare their areas.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|a1 = ImageArea(7, 10)<br>a2 = ImageArea(35, 2)<br>a3 = ImageArea(8, 9)<br>print(a1 == a2)<br>print(a1 != a3)         |True<br>True          |
|a1 = ImageArea(7, 10)<br>a2 = ImageArea(35, 2)<br>a3 = ImageArea(8, 9)<br>print(a1 != a2)<br>print(a1 >= a3) |False<br>False |
|a1 = ImageArea(7, 10)<br>a2 = ImageArea(35, 2)<br>a3 = ImageArea(8, 9)<br>print(a1 <= a2)<br>print(a1 < a3)  |True<br>True |
