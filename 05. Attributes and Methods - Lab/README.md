## **1.	Store -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/05.%20Attributes%20and%20Methods%20-%20Lab/01_store.py)
Create a class called Store. Upon initialization it should receive a name (str), type (str), capacity (int). The store should also have an attribute called items (dictionary that stores name of an item and its quantity). The class should have 4 methods:  
•	from_size (name:str, type:str, size:int) – a new instance should be created with capacity which is 50% of the size  
•	add_item(item_name:str) – adds 1 to the quantity of the given item. On success, the method should return "{item_name} added to the store". If the addition is not possible, the following message should be returned "Not enough capacity in the store"  
•	remove_item(item_name:str, amount:int) – removes the given amount from the item. On success, it should return "{count} {item_name} removed from the store". Otherwise, the method should return "Cannot remove {count} {item_name}"  
•	__repr__() - returns a string representation in the format "{store_name} of type {store_type} with capacity {store_capacity}"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|first_store = Store("First store", "Fruit and Veg", 20)<br>second_store = Store.from_size("Second store", "Clothes", 500)<br><br>print(first_store)<br>print(second_store)<br><br>print(first_store.add_item("potato"))<br>print(second_store.add_item("jeans"))<br>print(first_store.remove_item("tomatoes", 1))<br>print(second_store.remove_item("jeans", 1))         |First store of type Fruit and Veg with capacity 20<br>Second store of type Clothes with capacity 250<br>potato added to the store<br>jeans added to the store<br>Cannot remove 1 tomatoes<br>1 jeans removed from the store          |


## **2.	Integer -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/05.%20Attributes%20and%20Methods%20-%20Lab/02_integer.py)
Create a class called Integer. Upon initialization it should receive a single parameter value (int). It should have 4 methods:  
•	from_float(value) - creates a new instance by flooring the provided floating number. If the value is not a float return a message "value is not a float"  
•	from_roman(value) – creates a new instance by converting the roman number (as string) to an integer  
•	from_string(value) - creates a new instance by converting the string to an integer (if the value cannot be converted, return a message "wrong type")  
•	add(integer:Integer) – adds the values of the two instances and returns the result (if the integer is not an instance of Integer, return the message "number should be an Integer instance")

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|first_num = Integer(10)<br>second_num = Integer.from_roman("IV")<br><br>print(Integer.from_float("2.6"))<br>print(Integer.from_string(2.6))<br>print(first_num.add(second_num))          |value is not a float<br>wrong type<br>14          |



## **3.	Calculator -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/05.%20Attributes%20and%20Methods%20-%20Lab/03_calculator.py)
Create a class called Calculator that has the following static methods:  
•	add(*args) – sums all the arguments passed to the function and returns the result  
•	multiply(*args) – multiplies all the numbers and returns the result  
•	divide(*args) – divides all the numbers and returns the result  
•	subtract(*args) – subtracts all the numbers and returns the result  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|print(Calculator.add(5, 10, 4))<br>print(Calculator.multiply(1, 2, 3, 5))<br>print(Calculator.divide(100, 2))<br>print(Calculator.subtract(90, 20, -50, 43, 7))          |19<br>30<br>50.0<br>70          |



## **04.	Hotel Rooms -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/05.%20Attributes%20and%20Methods%20-%20Lab/hotel_rooms_04/project)
In a folder called project create two files: hotel.py and room.py  
In the room.py file create a class called Room. Upon initialization it should receive a number (int) and a capacity (int). It should also have an attribute called guests (0 upon initialization) and is_taken (False upon initialization). The class should have 2 methods:  
•	take_room(people) – if the room is not taken, and there is enough space, the guests take the room. Otherwise, the method should return "Room number {number} cannot be taken"  
•	free_room() – if the room is taken, free it. Otherwise, return "Room number {number} is not taken"  
In the hotel.py file create a class called Hotel. Upon initialization it should receive a name (str). It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 upon initialization). The class should have 5 more methods:  
•	from_stars(stars_count) – creates a new instance with name "{stars_count} stars Hotel"  
•	add_room(room) – add the room to the list of rooms  
•	take_room(room_number, people) – find the room with that number and try to accommodate the guests in the room  
•	free_room(room_number) – find the room with that number and free it  
•	print_status() – prints information about the hotel in the following format:  
 
Hotel {name} has {guests} total guests  
Free rooms: {numbers of all free rooms separated by comma and space}  
Taken rooms: {numbers of all taken rooms separated by comma and space}  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|from project.hotel import Hotel<br>from project.room import Room<br><br>hotel = Hotel.from_stars(5)<br><br>first_room = Room(1, 3)<br>second_room = Room(2, 2)<br>third_room = Room(3, 1)<br><br>hotel.add_room(first_room)<br>hotel.add_room(second_room)<br>hotel.add_room(third_room)<br><br>hotel.take_room(1, 4)<br>hotel.take_room(1, 2)<br>hotel.take_room(3, 1)<br>hotel.take_room(3, 1)<br><br>hotel.print_status()         |Hotel 5 stars Hotel has 3 total guests<br>Free rooms: 2<br>Taken rooms: 1, 3          |


