## **01.	Wild Cat Zoo -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/08.%20Encapsulation%20-%20Exercise/wild_cat_zoo_01/project)
Class Lion  
Attributes  
Public attribute name: string  
Public attribute gender: string  
Public attribute age: number  
Methods  
\_\_init\_\_(name, gender, age) - set all the attributes to the given ones  
get_needs() - returns the number 50 (amount of money needed to tend the animal)  
\_\_repr\_\_() - returns string representation of the lion in the format: "Name: {name}, Age: {age}, Gender: {gender}"  

Class Tiger  
Attributes  
Public attribute name: string  
Public attribute gender: string  
Public attribute age: number  
Methods  
\_\_init\_\_(name, gender, age) - set all the attributes to the given ones  
get_needs() - returns the number 45 (amount of money needed to tend the animal)  
\_\_repr\_\_() - returns string representation of the tiger in the format: "Name: {name}, Age: {age}, Gender: {gender}"  

Class Cheetah  
Attributes  
Public attribute name: string  
Public attribute gender: string  
Public attribute age: number  
Methods  
\_\_init\_\_(name, gender, age) - set all the attributes to the given ones  
get_needs() - returns the number 60 (amount of money needed to tend the animal)  
\_\_repr\_\_() - returns string representation of the cheetah in the format: "Name: {name}, Age: {age}, Gender: {gender}"  

Class Keeper  
Attributes  
Public attribute name: string  
Public attribute age: number  
Public attribute salary: number  
Methods  
\_\_init\_\_(name, age, salary) - set all the attributes to the given ones  
\_\_repr\_\_() - returns string representation of the keeper in the format: "Name: {name}, Age: {age}, Salary: {salary}"  

Class Caretaker  
Attributes  
Public attribute name: string  
Public attribute age: number  
Public attribute salary: number  
Methods  
\_\_init\_\_(name, age, salary) - set all the attributes to the given ones  
\_\_repr\_\_() - returns string representation of the caretaker in the format: "Name: {name}, Age: {age}, Salary: {salary}"  

Class Vet  
Attributes  
Public attribute name: string  
Public attribute age: number  
Public attribute salary: number  
Methods  
\_\_init\_\_(name, age, salary) - set all the attributes to the given ones  
\_\_repr\_\_() - returns string representation of the vet in the format: "Name: {name}, Age: {age}, Salary: {salary}"  

Class Zoo  
Attributes  
Private attribute animal_capacity: number  
Private attribute workers_capacity: number  
Private attribute budget: number  
Public attribute name: string  
Public attribute animals: list (empty upon initialization)  
Public attribute workers: list (empty upon initialization)  
Methods  
\_\_init\_\_(name, budget, animlal_capacity, workers_capacity) - set the attributes to the given ones  
- add_animal(animal, price)  
If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals list, reduce the budget and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"  
If you have capacity, but no budget, return "Not enough budget"  
In any other case, you don't have space and you should return "Not enough space for animal"  
- hire_worker(worker)  
If you have enough space for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"  
Otherwise return "Not enough space for worker"  
- fire_worker(worker_name)  
If there is a worker with that name in the workers list, remove him and return "{worker_name} fired successfully"  
Otherwise return "There is no {worker_name} in the zoo"  
- pay_workers()  
If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"  
Otherwise return "You have no budget to pay your workers. They are unhappy"  
- tend_animals()  
If you have enough budget to tend the animals reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"  
Otherwise return "You have no budget to tend the animals. They are unhappy."  
- profit(amount)  
Increase the budget with the given amount of profit  
- animals_status()  
Returns the following string:  
You have {total_animals_count} animals  
----- {amount_of_lions} Lions:  
{lion1}  
…  
----- {amount_of_tigers} Tigers:  
{tiger1}  
…  
----- {amount_of_cheetahs} Cheetahs:  
{cheetah1}  
…  
Hint: use the \_\_repr\_\_ methods of the animals to print them on the console  
- workers_status()  
Returns the following string:  
You have {total_workers_count} workers  
----- {amount_of_keepers} Keepers:  
{keeper1}  
…  
----- {amount_of_caretakers} Caretakers:  
{caretaker1}  
…  
----- {amount_of_vetes} Vets:  
{vet1}  
…  
Hint: use the \_\_repr\_\_ methods of the workers to print them on the console  


*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|zoo = Zoo("Zootopia", 3000, 5, 8)<br><br># Animals creation<br>animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]<br><br># Animal prices<br>prices = [200, 190, 204, 156, 211, 140]<br><br># Workers creation<br>workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]<br><br># Adding all animals<br>for i in range(len(animals)):<br>    animal = animals[i]<br>    price = prices[i]<br>    print(zoo.add_animal(animal, price))<br><br># Adding all workers<br>for worker in workers:<br>    print(zoo.hire_worker(worker))<br><br># Tending animals<br>print(zoo.tend_animals())<br><br># Paying keepers<br>print(zoo.pay_workers())<br><br># Fireing worker<br>print(zoo.fire_worker("Adam"))<br><br># Printing statuses<br>print(zoo.animals_status())<br>print(zoo.workers_status())          |Cheeto the Cheetah added to the zoo<br>Cheetia the Cheetah added to the zoo<br>Simba the Lion added to the zoo<br>Zuba the Tiger added to the zoo<br>Tigeria the Tiger added to the zoo<br>Not enough space for animal<br>John the Keeper hired successfully<br>Adam the Keeper hired successfully<br>Anna the Keeper hired successfully<br>Bill the Caretaker hired successfully<br>Marie the Caretaker hired successfully<br>Stacy the Caretaker hired successfully<br>Peter the Vet hired successfully<br>Kasey the Vet hired successfully<br>Not enough space for worker<br>You tended all the animals. They are happy. Budget left: 1779<br>You payed your workers. They are happy. Budget left: 611<br>Adam fired successfully<br>You have 5 animals<br>----- 1 Lions:<br>Name: Simba, Age: 4, Gender: Male<br>----- 2 Tigers:<br>Name: Zuba, Age: 3, Gender: Male<br>Name: Tigeria, Age: 1, Gender: Female<br>----- 2 Cheetahs:<br>Name: Cheeto, Age: 2, Gender: Male<br>Name: Cheetia, Age: 1, Gender: Female<br>You have 7 workers<br>----- 2 Keepers:<br>Name: John, Age: 26, Salary: 100<br>Name: Anna, Age: 31, Salary: 95<br>----- 3 Caretakers:<br>Name: Bill, Age: 21, Salary: 68<br>Name: Marie, Age: 32, Salary: 105<br>Name: Stacy, Age: 35, Salary: 140<br>----- 2 Vets:<br>Name: Peter, Age: 40, Salary: 300<br>Name: Kasey, Age: 37, Salary: 280         |




