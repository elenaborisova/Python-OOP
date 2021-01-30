## **01.	Test Worker -** [Source Code](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/test_worker_01/worker.py) - [Tests](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/tests/worker/test_worker.py)
Load provided skeleton in the IDE you use. Add new project Tests.  

Create a class WorkerTests  
Create the following tests:  
•	Test if the worker is initialized with correct name, salary and energy  
•	Test if the worker's energy is incremented after the rest method is called  
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0  
•	Test if the worker's money is increased by his salary correctly after the work method is called  
•	Test if the worker's energy is decreased after the work method is called	  
•	Test if the get_info method returns the proper string with correct values  




## **02.	Test Cat -** [Source Code](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/test_cat_02/cat.py) - [Tests](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/tests/cat/test_cat.py)
Create a class CatTests

Create the following tests:  
•	Cat's size is increased after eating  
•	Cat is fed after eating  
•	Cat cannot eat if already fed, raises an error  
•	Cat cannot fall asleep if not fed, raises an error  
•	Cat is not sleepy after sleeping  


## **03.	List -** [Source Code](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/list_03/integer_list.py) - [Tests](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/tests/integer_list/test_integer_list.py)
You are provided with a class IntegerList. It should only store integers. The initial integers should be set by constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the biggest number and get the index of an element. Your task is to test the class.

Constraints  
•	add operation, should add an element and returns the list.  
o	If the element is not an integer, a ValueError is thrown  
•	remove_index operation removes the element on that index and returns it.  
o	If the index is out of range, an IndexError is thrown  
•	\_\_init\_\_ should only take integers, and store them  
•	get should return the specific element   
o	If the index is out of range, an IndexError is thrown  
•	insert  
o	If the index is out of range, IndexError is thrown  
o	If the element is not an integer, ValueError is thrown  
•	get_biggest  
•	get_index  




## **04.	Car Manager -** [Source Code](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/car_manager_04/car.py) - [Tests](https://github.com/elenaborisova/Python-OOP/blob/main/19.%20Testing%20-%20Lab/tests/car/test_car.py)
You are provided with a simple project containing only one class - Car. The provided class is simple - its main point is to represent some of the functionality of a Car. Each car contains information about its make, model, fuel consumption, fuel amount and fuel capacity. Also, each Car can add some fuel to its tank by refueling and can travel distance by driving. In order to be driven, our Car needs to have enough fuel. Everything in the provided skeleton is working perfectly fine and you mustn't change it.

Your job now is to write unit tests on the provided project and its functionality. You should test every part of code inside the Car class:  
•	You should test the constructor  
•	You should test all the methods and validations inside the class  

Constraints  
•	Everything in the provided skeleton is working perfectly fine  
•	You mustn't change anything in the project structure  
•	Any part of validation should be tested  
•	There is no limit on the tests you can write but keep your attention on the main functionality  
