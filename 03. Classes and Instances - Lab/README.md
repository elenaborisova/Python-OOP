## **01.	Smartphone -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/03.%20Classes%20and%20Instances%20-%20Lab/01_smartphone.py)
Create a class called Smartphone. Upon initialization it should receive a memory (number). It should also have 2 other attributes: apps (empty list by default) and is_on (False by default). Create 3 methods:  
-	power() - sets is_on on True if the phone is off, otherwise sets it to False  
-	install(app, app_memory)   
o	If there is enough memory on the phone and it is on, install the app (add it to apps and decrease the memory of the phone) and return "Installing {app}"  
o	If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"  
o	Otherwise return "Not enough memory to install {app}"  
-	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"  
 
*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|smartphone = Smartphone(100)<br>print(smartphone.install("Facebook", 60))<br>smartphone.power()<br>print(smartphone.install("Facebook", 60))<br>print(smartphone.install("Messenger", 20))<br>print(smartphone.install("Instagram", 40))<br>print(smartphone.status())   |Turn on your phone to install Facebook<br>Installing Facebook<br>Installing Messenger<br>Not enough memory to install Instagram<br>Total apps: 2. Memory left: 20    |


## **02.	Vet -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/03.%20Classes%20and%20Instances%20-%20Lab/02_vet.py)
Create a class called Vet. Upon initialization it should receive a name (string). It should also have an instance attribute called animals (empty list by default). There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; space (5 by default). You have to create 3 more instance methods  
-	register_animal(animal_name)  
o	If there is space in the vet clinic add the animal to both animals lists and return a message: "{name} registered in the clinic"  
o	Otherwise return "Not enough space"  
-	unregister_animal(animal_name)  
o	If the animal is in the relevant vet list, remove it from both animals lists and return "{animal} unregistered successfully"  
o	Otherwise, return "{animal} not in the clinic"  
-	info() - returns "{vet_name} has {amount_of_his_animals} animals. {space_left_in_clinic} space left in clinic"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|peter = Vet("Peter")<br>george = Vet("George")<br>print(peter.register_animal("Tom"))<br>print(george.register_animal("Cory"))<br>print(peter.register_animal("Fishy"))<br>print(peter.register_animal("Bobby"))<br>print(george.register_animal("Kay"))<br>print(george.unregister_animal("Cory"))<br>print(peter.register_animal("Silky"))<br>print(peter.unregister_animal("Molly"))<br>print(peter.unregister_animal("Tom"))<br>print(peter.info())<br>print(george.info())  |Tom registered in the clinic<br>Cory registered in the clinic<br>Fishy registered in the clinic<br>Bobby registered in the clinic<br>Kay registered in the clinic<br>Cory unregistered successfully<br>Silky registered in the clinic<br>Molly not in the clinic<br>Tom unregistered successfully<br>Peter has 3 animals. 1 space left in clinic<br>George has 1 animals. 1 space left in clinic  |



## **03.	Glass -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/03.%20Classes%20and%20Instances%20-%20Lab/03_glass.py)
Create a class called Glass. Upon initialization it will not receive any parameters, you must create however an instance attribute called content which should be equal to 0. You should also create a class attribute called capacity which should be 250 ml. Create 3 more instance methods:  
-	fill(ml) - fill the glass with the given milliliters if there is enough space in it and return "Glass filled with {ml} ml", otherwise return "Cannot add {ml} ml"  
-	empty() - empty the glass and return "Glass is now empty"   
-	info() - returns info about the glass in the format "{space_left} ml left"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|glass = Glass()<br>print(glass.fill(100))<br>print(glass.fill(200))<br>print(glass.empty())<br>print(glass.fill(200))<br>print(glass.info())  |Glass filled with 100 ml<br>Cannot add 200 ml<br>Glass is now empty<br>Glass filled with 200 ml<br>50 ml left          |

