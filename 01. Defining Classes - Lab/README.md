## **01.	Rhombus of Stars -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/01_rhombus_of_stars.py)
Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1                  |*          |
|2                  |&nbsp;*<br>*&nbsp;*<br>&nbsp;*                |
|3                  |&nbsp;&nbsp;*<br>&nbsp;*<br>*&nbsp;*<br>&nbsp;*<br>&nbsp;&nbsp;*                   |




## **02.	Class Book -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/02_class_book.py)
Create a class called Book. It should have an __init__() method that should receive a name, author and pages (number).
Submit only the class in the judge system. 

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|book = Book("My Book", "Me", 200)<br>print(book.name)<br>print(book.author)<br>print(book.pages)     |My Book<br>Me<br>200          |






## **03.	Scope Mess -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/03_scope_mess.py)
Fix the code below, so it gives the expected output. Submit the fixed code in the judge system.

    x = "global"
    
    def outer():
        x = "local"
        
        def inner():
            x = "nonlocal"
            print("inner:", x)
        
        def change_global():
            x = "global: changed!"
        
        print("outer:", x)
        inner()
        print("outer:", x)
        change_global()
        
        
    print(x)
    outer()
    print(x)


*Examples*

|       Current Input       |      Exected Output       |
|---------------------------|---------------------------|
|global<br>outer: local<br>inner: nonlocal<br>outer: local<br>global  |global<br>outer: local<br>inner: nonlocal<br>outer: nonlocal<br>global: changed!  |






## **04.	Music -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/04_music.py)
Create class named Music that receives title, artist and lyrics upon initialization. The class should also have methods print_info() and play(). The print_info() method should return the following: 
'This is "{title}" from "{artist}"'. The play() method should return the lyrics. Submit only the class in the judge system. Test your code with your own examples.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|song = Music("Title", "Artist", "Lyrics")<br>print(song.print_info())<br>print(song.play())    |This is "Title" from "Artist"<br>Lyrics          |







## **05.	Cup -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/05_cup.py)
Create a class called Cup. Upon initialization it should receive size and quantity (a number representing how much liquid is in it). The class should also have a method called fill(milliliters) which will increase the amount of liquid in the cup with the given milliliters (if there is space in the cup, otherwise ignore). The cup should also have a status() method which will return the amount of free space left in the cup. Submit only the class in the judge system. Don't forget to test your code.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|cup = Cup(100, 50)<br>cup.fill(50)<br>cup.fill(10)<br>print(cup.status())  |0          |





## **06.	Flower -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/01.%20Defining%20Classes%20-%20Lab/06_flower.py)
Create a class called Flower. Upon initialization, the class should receive name and water_requirements. The flower should also have an attribute called is_happy (False by default) and a method called water(quantity), which will water the flower. If the water is greater than or equal of the requirements of the flower, it becomes happy. (set is_happy to True). The last method should be called status() and it should return "{name} is happy" if the flower is happy, otherwise it should return "{name} is not happy". Submit only the class in the judge system.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|flower = Flower("Lilly", 100)<br>flower.water(50)<br>print(flower.status())<br>flower.water(100)<br>print(flower.status())  |Lilly is not happy<br>Lilly is happy          |



