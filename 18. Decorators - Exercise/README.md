## **01.	Logged -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/01_logged.py)
Create a decorator called logged. It should return the name of the function that is being called and its parameters. It should also return the result of the execution of the function being called. See the examples for more clarification.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@logged<br>def func(*args):<br><pre>    return 3 + len(args)</pre><br>print(func(4, 4, 4))  |you called func(4, 4, 4)<br>it returned 6          |
|@logged<br>def sum_func(a, b):<br><pre>    return a + b</pre><br>print(sum_func(1, 4))  |you called sum_func(1, 4)<br>it returned 5  |






## **02.	Even Parameters -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/02_even_parameters.py)
Create a decorator function called even_parameters. It should check if all parameters passed to a function are even numbers and only then execute the function and return the result. Otherwise don't execute the function and return "Please use only even numbers!"

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@even_parameters<br>def add(a, b):<br><pre>    return a + b</pre><br><br>print(add(2, 4))<br>print(add("Peter", 1))   |6<br>Please use only even numbers!         |
|@even_parameters<br>def multiply(*nums):<br><pre>    result = 1<br>    for num in nums:<br>        result *= num<br>    return result</pre><br><br>print(multiply(2, 4, 6, 8))<br>print(multiply(2, 4, 9, 8)) |384<br>Please use only even numbers! |







## **03.	Bold, Italic, Underline -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/03_bold_italic_underline.py)
Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@make_bold<br>@make_italic<br>@make_underline<br>def greet(name):<br><pre>    return f"Hello, {name}"<pre><br><br>print(greet("Peter"))          |\<b>\<i>\<u>Hello, Peter</u></i></b>          |
|@make_bold<br>@make_italic<br>@make_underline<br>def greet_all(*args):<br><pre>    return f"Hello, {', '.join(args)}"</pre><br><br>print(greet_all("Peter", "George"))  |<b><i><u>Hello, Peter, George</u></i></b> |






## **04.	Type Check -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/04_type_check.py)
Create a decorator called type_check. It should receive a type (int/float/str/…) and it should check if the parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and return the result, otherwise return "Bad Type".

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@type_check(int)<br>def times2(num):<br><pre>    return num*2</pre><br>print(times2(2))<br>print(times2('Not A Number'))          |4<br>Bad Type         |
|@type_check(str)<br>def first_letter(word):<br><pre>    return word[0]</pre><br><br>print(first_letter('Hello World'))<br>print(first_letter(['Not', 'A', 'String'])) |H<br>Bad Type |






## **05.	Cache -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/05_cache.py)
Create a decorator called cache. It should store all the returned values of e recursive function fibonacci. You are provided with this code:

        def cache(func):
            # TODO: Implement

        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
                
You need to create a dictionary called log that will store all the n's (keys) and the returned results (values) and attach that dictionary to the fibonacci function as a variable called log, so when you call it, it returns that dictionary. For more clarification, see the examples

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|fibonacci(3)<br>print(fibonacci.log)          |{1: 1, 0: 0, 2: 1, 3: 2}          |
|fibonacci(4)<br>print(fibonacci.log) |{1: 1, 0: 0, 2: 1, 3: 2, 4: 3} |






## **06.	HTML Tags -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/06_html_tags.py)
Create a decorator called tags. It should receive an html tag as a parameter, wrap the result of a function with the given tag and return the new result. For more clarification, see the examples below

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@tags('p')<br>def join_strings(*args):<br><pre>    return "".join(args)</pre><br><br>print(join_strings("Hello", " you!"))          |<p>Hello you!</p>          |
|@tags('h1')<br>def to_upper(text):<br><pre>    return text.upper()</pre><br><br>print(to_upper('hello')) |<h1>HELLO</h1> |







## **07.	Execution Time -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/07_execution_time.py)
Create a decorator called exec_time. It should calculate how much time a function needs to be executed. See the examples for more clarification.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@exec_time<br>def loop(start, end):<br><pre>    total = 0<br>    for x in range(start, end):<br>        total += x<br>    return total</pre><br><br>print(loop(1, 10000000))        |0.8342537879943848         |
|@exec_time<br>def concatenate(strings):<br><pre>    result = ""<br>    for string in strings:<br>        result += string<br>    return result</pre><br><br>print(concatenate(["a" for i in range(1000000)])) |0.14537858963012695 |





## **08.	*Store Results -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/18.%20Decorators%20-%20Exercise/08_store_results.py)
Create a class called store_results. It should be used as decorator and store information about the executed functions in a file called results.txt in the format: "Function {func_name} was add called. Result: {func_result}"

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|@store_results<br><pre>def add(a, b):<br>    return a + b<br><br>@store_results<br>def mult(a, b):<br>    return a * b<br><br>add(2, 2)<br>mult(6, 4)         |Function 'add' was called. Result: 4<br>Function 'mult' was called. Result: 24          |



