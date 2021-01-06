## **01.	Vehicle -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/12.%20Polymorphism%20and%20Magic%20Methods%20-%20Exercise/01_vehicle.py)
Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both have fuel_quantity, fuel_consumption in liters per km and can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air conditioners and their fuel consumption per km when driving is increased by 0.9 liters for the car and with 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank and when it's refueled it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|car = Car(20, 5)<br>car.drive(3)<br>print(car.fuel_quantity)<br>car.refuel(10)<br>print(car.fuel_quantity)          |2.299999999999997<br>12.299999999999997          |
|truck = Truck(100, 15)<br>truck.drive(5)<br>print(truck.fuel_quantity)<br>truck.refuel(50)<br>print(truck.fuel_quantity) |17.0<br>64.5  |



## **02.	Groups -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/12.%20Polymorphism%20and%20Magic%20Methods%20-%20Exercise/02_groups.py)
Create a class called Person. Upon initialization it will receive a name (str) and a surname (str). Create another class called Group. Upon initialization it should receive a name (str) and people (list of Person instances). Implement the needed magic methods, so the test code below works

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|p0 = Person('Aliko', 'Dangote')<br>p1 = Person('Bill', 'Gates')<br>p2 = Person('Warren', 'Buffet')<br>p3 = Person('Elon', 'Musk')<br>p4 = p2 + p3<br><br>first_group = Group('__VIP__', [p0, p1, p2])<br>second_group = Group('Special', [p3, p4])<br>third_group = first_group + second_group<br><br>print(len(first_group))<br>print(second_group)<br>print(third_group[0])<br><br>for person in third_group:<br>    print(person)         |3<br>Group Special with members Elon Musk, Warren Musk<br>Person 0: Aliko Dangote<br>Person 0: Aliko Dangote<br>Person 1: Bill Gates<br>Person 2: Warren Buffet<br>Person 3: Elon Musk<br>Person 4: Warren Musk          |



## **03.	Account -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/12.%20Polymorphism%20and%20Magic%20Methods%20-%20Exercise/03_account.py)
Create a single class called Account. Upon initialization, it should receive owner (str) and amount (int, optional, 0 by default). It should also have an attribute called _transactions (empty list upon initialization). Create the following methods:  
•	add_transaction(amount) – if the amount is not an integer, raise ValueError with message "please use int for amount", otherwise, add the amount to the transactions  
•	balance() – property that returns sum of the amount and all the transactions  
•	validate_transaction(account: Account, amount_to_add) – if the transaction is possible, add it. If the balance becomes less than zero, raise ValueError with message "sorry cannot go in debt!" and break the transaction. Otherwise, complete it and return a message "New balance: {account_ballance}"  
Implement the correct magic methods, so the code in the example bellow works properly

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|acc = Account('bob', 10)<br>acc2 = Account('john')<br>print(acc)<br>print(repr(acc))<br>acc.add_transaction(20)<br>acc.add_transaction(-20)<br>acc.add_transaction(30)<br>print(acc.balance)<br>print(len(acc))<br>for transaction in acc:<br>    print(transaction)<br>print(acc[1])<br>print(list(reversed(acc)))<br>acc2.add_transaction(10)<br>acc2.add_transaction(60)<br>print(acc > acc2)<br>print(acc >= acc2)<br>print(acc < acc2)<br>print(acc <= acc2)<br>print(acc == acc2)<br>print(acc != acc2)<br>acc3 = acc + acc2<br>print(acc3)<br>print(acc3._transactions)          |Account of bob with starting amount: 10<br>Account(bob, 10)<br>40<br>3<br>20<br>-20<br>30<br>-20<br>[30, -20, 20]<br>False<br>False<br>True<br>True<br>False<br>True<br>Account of bob&john with starting amount: 10<br>[20, -20, 30, 10, 60]          |


## **04.	Wild Farm -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/12.%20Polymorphism%20and%20Magic%20Methods%20-%20Exercise/wild_farm_04/project)
Your task is to create a class hierarchy like the described below. The Animal, Bird, Mammal and Food classes should be abstract:  
In the food.py file implement the following classes:  
•	Food - quantity (int) - abstract class  
o	Vegetable  
o	Fruit  
o	Meat  
o	Seed  

In the animal.py file implement the Animal, Bird and Mammal classes. In the birds.py file implement the bird classes and in the mammals.py file implement the mammal classes  
•	Animal - name (string), weight (float), food_eaten (attribute, 0 upon initialization) - abstract class  
o	Bird - wing_size (float) - abstract class  
	Owl  
	Hen  
o	Mammal - living_region (string) - abstract class  
	Mouse  
	Dog  
	Cat  
	Tiger  

All animals should also have the ability to ask for food by producing a sound. make_sound() method that returns the sound:  
•	Owl - "Hoot Hoot"  
•	Hen - "Cluck"  
•	Mouse - "Squeak"  
•	Dog - "Woof!"  
•	Cat - "Meow"  
•	Tiger - "ROAR!!!"  

Now use the classes that you have created to instantiate some animals and feed them. Add method feed(food) where the food will be instance of some of the food classes.  
Animals will only eat a certain type of food, as follows:  
•	Hens eat everything  
•	Mice eat vegetables and fruits  
•	Cats eat vegetables and meat  
•	Tigers, Dogs and Owls eat only meat  
If you try to give an animal a different type of food, it will not eat it and you should return:  
•	"{AnimalType} does not eat {FoodType}!"  
The weight of an animal will increase with every piece of food it eats, as follows:  
•	Hen - 0.35  
•	Owl - 0.25  
•	Mouse - 0.10  
•	Cat - 0.30  
•	Dog - 0.40  
•	Tiger - 1.00  

Override the __repr__() method to print the information about an animal in the formats:  
•	Birds - "{AnimalType} [{AnimalName}, {WingSize}, {AnimalWeight}, {FoodEaten}]"  
•	Mammals - "{AnimalType} [{AnimalName}, {AnimalWeight}, {AnimalLivingRegion}, {FoodEaten}]"

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|owl = Owl("Pip", 10, 10)<br>print(owl)<br>meat = Meat(4)<br>print(owl.make_sound())<br>owl.feed(meat)<br>veg = Vegetable(1)<br>print(owl.feed(veg))<br>print(owl)          |Owl [Pip, 10, 10, 0]<br>Hoot Hoot<br>Owl does not eat Vegetable!<br>Owl [Pip, 10, 11.0, 4]          |
|hen = Hen("Harry", 10, 10)<br>veg = Vegetable(3)<br>fruit = Fruit(5)<br>meat = Meat(1)<br>print(hen)<br>print(hen.make_sound())<br>hen.feed(veg)<br>hen.feed(fruit)<br>hen.feed(meat)<br>print(hen) |Hen [Harry, 10, 10, 0]<br>Cluck<br>Hen [Harry, 10, 13.15, 9] |


