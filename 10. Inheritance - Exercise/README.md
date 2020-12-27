## **Problem 1.	Person -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/person_01/project)
You are asked to model an application for storing data about people. You should be able to have a Person and a Child. The child derives from the person. Every person has public attributes name and age. Your task is to model the application.

Create a Child class that inherits Person and has the same constructor definition. However, do not copy the code from the Person class - reuse the Person class's constructor.



## **Problem 2.	Zoo -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/zoo_02/project)
Create a zoo which contains the following classes: Animal (Base Class). Reptile and Mammal inherit Animal. Lizard and Snake inherit from Reptile, and Gorilla and Bear inherit from Mammal.

Each class, except the Animal class, should inherit from another class. The Animal class should have private attribute name – string and getter for the name.  
Every class should have constructor, which accepts one parameter: name  



## **Problem 3.	Players and Monsters -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/players_and_monsters_03/project)
Your task is to create the following game hierarchy: Hero (Base Class). Elf, Wizard, Knight inherit from Hero. MuseElf inherits from Elf, DarkWizard inherits from Wizard, SoulMaster inherits from DarkWizard. DarkKnight inherits from Knight, BladeKnight inherits from DarkKnight.

Create a class Hero. It should contain the following attributes:  
•	username - string  
•	level – int  
Override the __repr__() method of the base class so it returns: "{name} of type {class_name} has level {level}"




## **Problem 4.	Need for Speed -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/need_for_speed_04/project)
Create the following hierarchy with the following classes: Vehicle (Base Class), Motorcycle and Car inherit from Vehicle. RaceMotorcycle and CrossMotorcycle inherit from Motorcycle. FamilyCar and SportCar inherits from Car.

Create a base class Vehicle. It should contain the following attributes:  
•	DEFAULT_FUEL_CONSUMPTION – float (constant)  
•	fuel_consumption – float  
•	fuel – float  
•	horse_power – int  
•	A public constructor which accepts (fuel, horse_power) and set the default fuel consumption on the attribute fuel_consumption

The class should have the following methods:  
•	drive(kilometers)  
o	The drive method should have a functionality to reduce the fuel based on the travelled kilometers and fuel consumption. Keep in mind that you can drive the vehicle only if you have enough fuel to finish the driving.  
The default fuel consumption for Vehicle is 1.25. Some of the classes have different default fuel consumption:  
•	SportCar – DEFAULT_FUEL_CONSUMPTION = 10  
•	RaceMotorcycle – DEFAULT_FUEL_CONSUMPTION = 8  
•	Car – DEFAULT_FUEL_CONSUMPTION = 3  




## **Problem 5.	Restaurant -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/restaurant_05/project)
Create a restaurant with the following classes and hierarchy:

The Product class should have the following attributes and getters for each of them:  
•	name – string  
•	price – float  

Beverage and Food classes are products. The Beverage class should have the following attributes and getter for the milliliters:  
•	name – string  
•	price – float  
•	milliliters – float

The Food class should have the following attributes and getter for the grams:  
•	name – string  
•	price – float  
•	grams – float  

HotBeverage and ColdBeverage are beverages and they accept the following parameters upon initialization: name, price, milliliters

Coffee and Tea are hot beverages. The Coffee class should have the following additional attributes and getter for the caffeine:  
•	COFFEE_MILLILITERS = 50 (constant)  
•	COFFEE_PRICE = 3.50 (constant)  
•	caffeine – float  

MainDish, Dessert and Starter are food. They all accept the following parameters upon initialization: name, price, grams. Dessert should accept one more parameter in its constructor:  
•	calories – float  
Crate a getter for the attribute calories.  

Make Salmon, Soup and Cake inherit MainDish, Starter and Dessert classes respectively.

A Cake must have the following attributes upon initialization:  
•	CAKE_GRAMS = 250 (constant)  
•	CAKE_CALORIES = 1000 (constant)  
•	CAKE_PRICE = 5 (constant)  

A Salmon should have the following attributes upon initialization:  
•	SALMON_GRAMS = 22 (constant)  




## **Problem 6.	Mix it -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/10.%20Inheritance%20-%20Exercise/mix_it_06/project)
Create the classes shown below with the following hierarchy:

Class Vehicle will get available_seats: int upon initialization. Classes Car, Bus and Plane will inherit class Vehicle.  
The Car class should have the following attributes:  
•	available_seats – int  
•	fuel_tank – int  
•	fuel_consumption – float  
•	fuel – float  
Create getter and setter for attribute fuel and validate the fuel not to exceed the fuel capacity.   

The class should have the following methods:  
•	drive(distance) – check if you have enough fuel to travel the given distance.Reduce the fuel if you've managed to drive the car and return the following message " We've enjoyed the travel!".  
•	refuel(liters) – check if you have enough space in the tank to take the given liters.Increase the fuel in the tank and return the liters available or return "Capacity reached!". To do this inherit CapacityMixin with method named get_capacity(capacity, amount) which will return the message above if the amount provided is bigger than the capacity, otherwise - the difference between the capacity and the given amount.  

The Bus class should have the following attributes:  
•	available_seats – int  
•	ticket_price – float  
•	tickets_sold = 0 at the beginning  
The class should have the following methods:  
•	get_ticket(tickets_count) – use method get_capacity from CapacityMixin to check if there are still seats available in the bus and track the current number of tickets sold.  
•	get_total_profit() – return the profit from the sold tickets  

The Plane class should have the following attributes:  
•	available_seats – int  
•	rows – int  
•	seats_per_row – int  
•	seats_available – empty dict

The class should have method buy_tickets(row_number, tickets_count):  
•	check if the given row number is valid and return the following message if it's not: "There is no row {row_number} in the plane!"  
•	check if you can sell the given tickets count in the desired row using the method get_capacity from CapacityMixin and return tickets_count if the number of tickets is available for sale in this row. Don't forget to update the seats_available dictionary after selling some tickets!  
•	If the number of tickets for the row number are not enough (smaller than the tickets_count) return the following message: "Not enough tickets on row {row_number}!"  

Class Technology will get memory: float and memory_taken: float upon initialization. Classes Laptop and SmarhPhone will inherit class Technology.  
The Laptop class should have the following attributes:  
•	memory – float  
•	memory_taken – float  
The class should have method install_software(software, software_memory):  
•	check if you have memory to install the software and return the memory left after the install if sucessfully, otherwise return "You don't have enough space for {software}!"

The SmartPhone class should have the following attributes:  
•	memory – float  
•	memory_taken – float  
The class should have method install_apps(app, app_memory):  
•	check if you have memory to install the app and return the memory left after the install if sucessfully, otherwise return "You don't have enough space for {app}!"

Class ParkingMall will get parking_lots: int upon initialization.   
The class should have method check_availability():  
•	using the get_capacity method from CapacityMixin class check if there are any slots available in the level and return "Parking lots available: {self.parking_lots} ". If there are no places available in this level return "There are no more parking lots!"

Classes Level1, Level2 and Level3 will inherit class ParkingMall. Level1 has 150 parking lots, Level2 has 100 parking lots and Level3 has 80 parking.

