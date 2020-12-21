## **01.	Person -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/07.%20Encapsulation%20-%20Lab/01_person.py)
Create a class called Person. Upon initialization it should receive name and age. Create private name and age attributes (cannot be accessed outside the class). Create two instance methods called get_name and get_age to return the values of the private attributes.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|person = Person("George", 32)<br>print(person.get_name())<br>print(person.get_age())          |George<br>32         |




## **02.	Email Validator -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/07.%20Encapsulation%20-%20Lab/02_email_validator.py)
Create a class called EmailValidator. Upon initialization it should receive min_length (of the username; example: in "peter@gmail.com" "peter" is the username), mails (list of the valid mails; example: "gmail", "abv"), domains (list of valid domains; example: "com", "net"). Create three private methods:  
-	validate_name(name) - returns whether the name is greater than or equal to the min_length (True/False)  
-	validate_mail(mail) - returns whether the mail is in the possible mails list (True/False)  
-	validate_domain(domain) - returns whether the domain is in the possible domains list (True/False)  
Create one public method:  
-	validate(email) - using the three private methods returns whether the email is valid (True/False)  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|mails = ["gmail", "softuni"]<br>domains = ["com", "bg"]<br>email_validator = EmailValidator(6, mails, domains)<br>print(email_validator.validate("pe77er@gmail.com"))<br>print(email_validator.validate("georgios@gmail.net"))<br>print(email_validator.validate("stamatito@abv.net"))<br>print(email_validator.validate("abv@softuni.bg"))          |True<br>False<br>False<br>False          |



## **03.	Mammal -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/07.%20Encapsulation%20-%20Lab/03_mammal.py)
Create a class called Mammal. Upon initialization it should receive a name, type and sound. Create private class attribute called kingdom and set it to be "animals". Create three more instance methods:  
-	make_sound() - returns a string in the format "{name} makes {sound}"  
-	get_kingdom() - returns the private kingdom attribute  
-	info() - returns a string in the format "{name} is of type {type}"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|mammal = Mammal("Dog", "Domestic", "Bark")<br>print(mammal.make_sound())<br>print(mammal.get_kingdom())<br>print(mammal.info())          |Dog makes Bark<br>animals<br>Dog is of type Domestic          |




## **04.	Account -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/07.%20Encapsulation%20-%20Lab/04_account.py)
Create a class called Account. Upon initialization it should receive an id, balance and pin (all numbers). The pin and the id should be private instance attributes and the balance should be public attribute. Create two public instance methods:  
-	get_id(pin) - if the given pin is correct, return the id, otherwise return "Wrong pin"  
-	change_pin(old_pin, new_pin) - if the old pin is correct, change it to the new one and return "Pin changed", otherwise return "Wrong pin"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|account = Account(8827312, 100, 3421)<br>print(account.get_id(1111))<br>print(account.get_id(3421))<br>print(account.balance)<br>print(account.change_pin(2212, 4321))<br>print(account.change_pin(3421, 1234))          |Wrong pin<br>8827312<br>100<br>Wrong pin<br>Pin changed         |

