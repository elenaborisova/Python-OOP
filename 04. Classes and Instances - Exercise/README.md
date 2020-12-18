## **01.	Point -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/01_point.py)
Create a class called Point. Upon initialization it should receive x and y (numbers). Create 3 instance methods:  
-	set_x(new_x) - changes the x value of the point  
-	set_y(new_y) - changes the y value of the point  
-	distance(x, y) - returns the distance between the point and the provided coordinates  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|p = Point(2, 4)<br>p.set_x(3)<br>p.set_y(5)<br>print(p.distance(10, 2))  |7.615773105863909          |


## **02.	Circle -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/02_circle.py)
Create a class called Circle. Upon initialization it should receive a radius (number). Create a class attribute called pi which should be equal to 3.14. Create 3 instance methods:  
-	set_radius(new_radius) - changes the radius  
-	get_area() - returns the area of the circle  
-	get_circumference() - returns the circumference of the circle  
The area should be rounded to the 2nd decimal.  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|circle = Circle(10)<br>circle.set_radius(12)<br>print(circle.get_area())<br>print(circle.get_circumference())          |452.16<br>75.36          |



## **03.	Account -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/03_account.py)
Create a class called Account. Upon initialization it should receive id (number), name (string), balance (number; optional; 0 by default). The class should also have 3 instance methods:  
-	credit(amount) - add the amount to the balance and return the new balance  
-	debit(amount) - if the amount is less than or equal to the balance, reduce the balance by the amount and return the new balance. Otherwise return "Amount exceeded balance"  
-	info() - returns "User {name} with account {id} has {balance} balance"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|account = Account(1234, "George", 1000)<br>print(account.credit(500))<br>print(account.debit(1500))<br>print(account.info())          |1500<br>0<br>User George with account 1234 has 0 balance          |
|account = Account(5411256, "Peter")<br>print(account.debit(500))<br>print(account.credit(1000))<br>print(account.debit(500))<br>print(account.info()) |Amount exceeded balance<br>1000<br>500<br>User Peter with account 5411256 has 500 balance |



## **04.	Employee -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/04_employee.py)
Create class Employee. Upon initialization it should receive id (number), first_name (string), last_name (string), salary (number). Create 3 more instance methods:  
-	get_full_name() - returns "{first_name} {last_name}"  
-	get_annual_salary() - returns the salary for 12 months  
-	raise_salary(amount) - increase the salary by the given amount and return the new salary  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|employee = Employee(744423129, "John", "Smith", 1000)<br>print(employee.get_full_name())<br>print(employee.raise_salary(500))<br>print(employee.get_annual_salary())          |John Smith<br>1500<br>18000         |



## **05.	Time -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/05_time.py)
Create a class called Time. Upon initialization it should receive hours, minutes and seconds (numbers). The class should also have class attributes max_hours equal to 23, max_minutes equal to 59 and max_seconds equal to 59. You should also create 3 instance methods:  
-	set_time(hours, minutes, seconds) - update the time  
-	get_time() - returns "{hh}:{mm}:{ss}"  
-	next_second() - update the time with one second (use the class attributes for validation) and return the new time (using the get_time() method)  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|time = Time(9, 30, 59)<br>print(time.next_second())          |09:31:00          |
|time = Time(10, 59, 59)<br>print(time.next_second())        |11:00:00 |
|time = Time(23, 59, 59)<br>print(time.next_second())     |00:00:00 |



## **06.	Pizza Delivery -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/04.%20Classes%20and%20Instances%20-%20Exercise/06_pizza_delivery.py)
Create a class called PizzaDelivery. Upon initialization it should receive name(string), price(float) and ingredients (dict). The class should also have an attribute ordered set to false by default. You should also create 3 instance methods:  
-	add_extra(ingredient: str, quantity: int, ingredient_price: float):  
o	if we already have this ingredient in our pizza increase the ingredient quantity with the given one and update the pizza price by adding the amount for the additional ingredients  
o	if we don't have this ingredient in our pizza, we should add it and update the pizza price  
  
-	remove_ingredient(ingredient: str, quantity: int, ingredient_price: float):  
o	if we don't have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {name}!"  
o	if we have the ingredient, but we try to remove more than we have available we should return the following message "Please check again the desired quantity of {ingredient}!", otherwise remove the given quantity of the ingredient and update the pizza price  

-	pizza_ordered() – set the attribute ordered to True and return the following message "You've ordered pizza {name} prepared with {all ingredients and their quantities separated with coma and space} and the price will be {price}lv.". Please have in mind that once the pizza is ordered no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared and we can't make any changes!"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})<br>Margarita.add_extra('mozzarella', 1, 0.5)<br>Margarita.add_extra('cheese', 1, 1)<br>Margarita.remove_ingredient('cheese', 1, 1)<br>print(Margarita.remove_ingredient('bacon', 1, 2.5))<br>print(Margarita.remove_ingredient('tomatoes', 2, 0.5))<br>Margarita.remove_ingredient('cheese', 2, 1)<br>print(Margarita.pizza_ordered())<br>print(Margarita.add_extra('cheese', 1, 1))     |Wrong ingredient selected! We do not use bacon in Margarita!<br>Please check again the desired quantity of tomatoes!<br>You've ordered pizza Margarita prepared with cheese: 0, tomatoes: 1, mozzarella: 1 and the price will be 9.5lv.<br>Pizza Margarita already prepared and we can't make any changes!        |





## **07.	Library -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/04.%20Classes%20and%20Instances%20-%20Exercise/library_07/project)
Create class called Library, where the information regarding the users and books rented/available will be stored. Create another one called User, where the information for each of the library users will be stored: user id, username and file with records of the books rented by the current user.  

Class Library  
Upon initialization you won't receive anything. The class should have the following attributes:   
o	user_records – empty list which will store the users (users objects) of the library  
o	books_available – empty dictionary which will keep information regarding the authors (keys) and the books available for each of the authors (list)  
o	rented_books – empty dictionary with usernames for keys and another dictionary as value in which the book names will be the keys and days to return the value ({usernames: {book names: days left}}).  
You should also create 3 instance methods:  
-	add_user(user: User):  
o	add the user if we do not have him/her in the library records already, otherwise return the message "User with id = {user_id} already registered in the library!"  
  
-	remove_user(user: User):  
o	remove the user from the library records if available, otherwise return the message "We could not find such user to remove!"  

-	change_username(user_id: int, new_username: str):  
o	change the username with the new provided and return the message "Username successfully changed to: {new_username} for userid: {user_id}" if there is a  record with the same user id in the library and the username is different than the provided one.   
o	If the username is the same for this id return the following message "Please check again the provided username - it should be different than the username used so far!".  
o	If there is no record for the provided id return "There is no user with id = {user_id}!"  

Class User  
Upon initialization it should receive user_id(int) and username(string). The class should also have an attribute books which will be an empty list at the beginning. You should also create 3 instance methods:  
-	get_book(author: str, book_name: str, days_to_return: int, library: Library):  
o	if the book is available in the library add it to the books list for this user, update the library records (rented_books and available_books dicts) and return the following message: "{book_name} successfully rented for the next {days_to_return} days!"  
o	if it's already rented return the following message "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"  
  
-	return_book(author:str, book_name:str, library: Library):  
o	if the book is in the user's books list return it in the library (update books_available and rented_books class attributes) and remove it from the books list for this user  
o	otherwise return the following message "{username} doesn't have this book in his/her records!"  

-	info() – return a string containing the books currently rented by the user in ascending order separated by comma and space.  
-	You should also override the __string__ method in order to get a string in the following format "{user_id}, {username}, {books}"  

*Note: Please submit a zip file, containing a separate file for each of the classes, with the class names provided in the problem description and include them in project module in order to be able to make proper imports.*

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|from project.library import Library<br>from project.user import User<br><br>user = User(12, 'Peter')<br>library = Library()<br>library.add_user(user)<br>print(library.add_user(user))<br>library.remove_user(user)<br>print(library.remove_user(user))<br>library.add_user(user)<br>print(library.change_username(2, 'Igor'))<br>print(library.change_username(12, 'Peter'))<br>print(library.change_username(12, 'George'))<br><br>[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]<br>library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets', 'The Prisoner of Azkaban', 'The Goblet of Fire', 'The Order of the Phoenix', 'The Half-Blood Prince', 'The Deathly Hallows']})<br><br><br>user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)<br>print(library.books_available)<br>print(library.rented_books)<br>print(user.books)<br>print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))<br>print(user.return_book('J.K.Rowling', 'The Cursed Child', library))<br>user.return_book('J.K.Rowling', 'The Deathly Hallows', library)<br>print(library.books_available)<br>print(library.rented_books)<br>print(user.books)         |User with id = 12 already registered in the library!<br>We could not find such user to remove!<br>There is no user with id = 2!<br>Please check again the provided username - it should be different than the username used so far!<br>Username successfully changed to: George for userid: 12<br>12, George, []<br>{'J.K.Rowling': ['The Chamber of Secrets', 'The Prisoner of Azkaban', 'The Goblet of Fire', 'The Order of the Phoenix', 'The Half-Blood Prince']}<br>{'George': {'The Deathly Hallows': 17}}<br>['The Deathly Hallows']<br>The book "The Deathly Hallows" is already rented and will be available in 17 days!<br>George doesn't have this book in his/her records!<br>{'J.K.Rowling': ['The Chamber of Secrets', 'The Prisoner of Azkaban', 'The Goblet of Fire', 'The Order of the Phoenix', 'The Half-Blood Prince', 'The Deathly Hallows']}<br>{'George': {}}<br>[]          |





