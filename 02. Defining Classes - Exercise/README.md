## **01.	Car -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/02.%20Defining%20Classes%20-%20Exercise/01_car.py)
Create a class called Car. Upon initialization it should receive a name, model and engine (all strings). Create a method called get_info() which will return a string in the following format: 
"This is {name} {model} with engine {engine}". 

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|car = Car("Kia", "Rio", "1.3L B3 I4")<br>print(car.get_info())   |This is Kia Rio with engine 1.3L B3 I4          |




## **02.	Shop -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/02.%20Defining%20Classes%20-%20Exercise/02_shop.py)
Create a class called Shop. Upon initialization it should receive a name (string) and items (list). Create a method called get_items_count() which should return the amount of items in the store.

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])<br>print(shop.get_items_count())   |3        |



## **03.	Hero -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/02.%20Defining%20Classes%20-%20Exercise/03_hero.py)
Create a class called Hero. Upon initialization it should receive a name (string) and health (number). Create two functions:  
- defend(damage) - Deal the given damage to the hero; if the health is 0 or less, set it to 0 and return "{name} was defeated".  
- heal(amount) - Increase the health of the hero with the given amount.  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|hero = Hero("Peter", 100)<br>print(hero.defend(50))<br>hero.heal(50)<br>print(hero.defend(99))<br>print(hero.defend(1))  |None<br>None<br>Peter was defeated          |



## **04.	Steam User -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/02.%20Defining%20Classes%20-%20Exercise/04_steam_user.py)
Create a class called SteamUser. Upon initialization it should receive username (string), games (list). It should also have an attribute called played_hours (0 by default). Add three methods to the class:  

-	play(game, hours)  
o	If the game is in the user games increase the played_hours by the given hours and return "{username} is playing {game}"  
o	Otherwise, return "{game} is not in library"  

-	buy_game(game)  
o	If the game is not already in the user's games, add it and return "{username} bought {game}"  
o	Otherwise return "{game} is already in your library"  

-	stats() - returns "{username} has {games_count} games. Total play time: {played_hours}"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])<br>print(user.play("Fortnite", 3))<br>print(user.play("Oxygen Not Included", 5))<br>print(user.buy_game("CS:GO"))<br>print(user.buy_game("Oxygen Not Included"))<br>print(user.play("Oxygen Not Included", 6))<br>print(user.stats())  |Peter is playing Fortnite<br>Oxygen Not Included not in library<br>CS:GO is already in your library<br>Peter bought Oxygen Not Included<br>Peter is playing Oxygen Not Included<br>Peter has 4 games. Total play time: 9 |




## **05.	Programmer -** [Solution](https://github.com/elenaborisova/Python-OOP/blob/main/02.%20Defining%20Classes%20-%20Exercise/05_programmer.py)
Create a class called Programmer. Upon initialization it should receive name (string), language (string), skills (integer). The class should have two methods:  

-	watch_course(course_name, language, skills_earned)  
o	If the programmer's language is the equal to the one on the course increase his skills with the given one and return a message "{programmer} watched {course_name}".  
o	Otherwise return "{name} does not know {language}".  

-	change_language(new_language, skills_needed)   
o	If the programmer has the skills and the language is different from his, change his language to the new one and return "{name} switched from {previous_language} to {new_language}".  
o	If the programmer has the skills, but the language is the same as his return "{name} already knows {language}".  
o	In the last case the programmer does not have the skills, so return "{name} needs {needed_skills} more skills" and don't change his language  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|programmer = Programmer("John", "Java", 50)<br>print(programmer.watch_course("Python Masterclass", "Python", 84))<br>print(programmer.change_language("Java", 30))<br>print(programmer.change_language("Python", 100))<br>print(programmer.watch_course("Java: zero to hero", "Java", 50))<br>print(programmer.change_language("Python", 100))<br>print(programmer.watch_course("Python Masterclass", "Python", 84))  |John does not know Python<br>John already knows Java<br>John needs 50 more skills<br>John watched Java: zero to hero<br>John switched from Java to Python<br>John watched Python Masterclass |




*Note: For the rest of the problems please submit a zip file, containing a separate file for each of the classes, with the class names provided in the problem description and include them in a module named project.*

## **06.	Pokemon Battle -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/02.%20Defining%20Classes%20-%20Exercise/pokemon_battle_06/project)
You are tasked to create two classes: a Pokemon class and a Trainer class. The Pokemon class should receive a name (string) and health (int) upon initialization. It should also have a method called pokemon_details that returns the information of the pokemon:  "{pokemon_name} with health {pokemon_health}"  
The Trainer class should receive a name (string). The Trainer should also have an attribute pokemon (list, empty by default). The Trainer has three methods:  

-	add_pokemon(pokemon: Pokemon)  
o	Add the pokemon to the collection. After adding the pokemon, it should return "Caught {pokemon_name} with health {pokemon_health}". Note: use the pokemon's details method.  
o	If the pokemon is already in the collection, it should return "This pokemon is already caught" 

-	release_pokemon(pokemon_name: String)   
o	Check if you have a pokemon with the name and remove it from the collection. It should return "You have released {pokemon_name}"  
o	If there isn't a pokemon with that name in the collection, return "Pokemon is not caught"  

-	trainer_data()  
o	The method returns the information of the trainer with his pokemon in this format:  
"Pokemon Trainer {trainer_name}  
 Pokemon count {the amount of pokemon caught}  
 - {pokemon_details}  
 ...  
 - {pokemon_details}  
"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|pokemon = Pokemon("Pikachu", 90)<br>print(pokemon.pokemon_details())<br>trainer = Trainer("Ash")<br>print(trainer.add_pokemon(pokemon))<br>second_pokemon = Pokemon("Charizard", 110)<br>print(trainer.add_pokemon(second_pokemon))<br>print(trainer.release_pokemon("Pikachu"))<br>print(trainer.trainer_data())  |Pikachu with health 90<br>Caught Pikachu with health 90<br>Caught Charizard with health 110<br>You have released Pikachu<br>Pokemon Trainer Ash<br>Pokemon count 1<br>- Charizard with health 110  |




## **07.	Guild System -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/02.%20Defining%20Classes%20-%20Exercise/guild_system_07/project)
You are tasked to create two classes: a Player class and a Guild class. The Player class should receive a name (string), hp (int) and mp (int) upon initialization. The Player also has 2 attributes: skills (empty dictionary) and guild set to "Unaffiliated" by default.  
The Player class should also have two methods:  

-	add_skill(skill_name, mana_cost)  
o	Add the skill to the collection. Return "Skill {skill_name} added to the collection of the player {player_name}"  
o	If the skill is already in the collection, return "Skill already added"  

-	player_info()  
o	Returns the player's information, including his/her skills, in this format:  
"Name: {player_name}  
 Guild: {guild_name}  
 HP: {hp}  
 MP: {mp}  
 ==={skill_name_1} – {skill_mana_cost}  
 ==={skill_name_2} – {skill_mana_cost}  
 ...  
 ==={skill_name_N} – {skill_mana_cost}  
"  

The Guild class receive a name {string}. It creates a list of players (empty by initialization). The class also has 3 methods:  
-	assign_player(player: Player)  
o	Add the player to the guild. Return "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.  
o	If the player is already in the guild, return "Player {player_name} is already in the guild."  
o	If the player is in another guild, return "Player {player_name} is in another guild."  

-	kick_player(player_name: String)  
o	Remove the player to the guild. Return "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class.  
o	If the isn't a player with that name in the guild, return "Player {player_name} is not in the guild."  

-	guild_info()  
o	Returns the guild's information, including the players in the guild, in this format:  
"Guild: {guild_name}  
 {player's info}  
"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|player = Player("George", 50, 100)<br>print(player.add_skill("Shield Break", 20))<br>print(player.player_info())<br>guild = Guild("UGT")<br>print(guild.assign_player(player))<br>print(guild.guild_info())   |Skill Shield Break added to the collection of the player George<br>Name: George<br>Guild: Unaffiliated<br>HP: 50<br>MP: 100<br>===Shield Break – 20<br><br>Welcome player George to the guild UGT<br>Guild: UGT<br>Name: George<br>Guild: UGT<br>HP: 50<br>MP: 100<br>===Shield Break – 20<br>     |








## **08.	Spoopify -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/02.%20Defining%20Classes%20-%20Exercise/spoopify_08/project)
You are tasked to create three classes: a Song class, an Album class and a Band class.  
The Song class should receive a name (string), length (float) and single (bool) upon initialization. It has one method:  

-	get_info()  
o	Returns the information of the song in this format: "{song name} – {song length}"  

The Album class should receive a name (string) and songs(one, many or none) as arguments upon initialization. It also has an attribute published (False by default). It has four methods:

-	add_song(song: Song)  
o	Adds the song to the album. Return "Song {song name} has been added to the album {name}."  
o	If the song is single, return "Cannot add {song name}. It's a single"  
o	If the album is published, return "Cannot add songs. Album is published."  
o	If the song is already added, return "Song is already in the album."  

-	remove_song(song_name: str)  
o	Removes the song with the given name and return "Removed song {song name} from album {name}.  
o	If the song is not in the album, return "Song is not in the album."  
o	If the album is published, return "Cannot remove songs. Album is published."  

-	publish()  
o	Publish the album and return "Album {name} has been published."  
o	If the album is published, return "Album {name} is already published."  

-	details()  
o	Returns the information of the album, with the songs in it, in this format:  
"Album {name}  
 == {first_song info}  
 == {second_song info}  
 …  
 == {n_song info}  
"  

The Band class should receive a name (string) upon initialization. It also has an attribute albums (empty list). It has three method:  
-	add_album(album: Album)  
o	Adds an album to the collection and returns "Band {name} has added their newest album {name}."  
o	If the album is already added, return "Band {name} already has {album name} in their library."  

-	remove_album(album_name: str)  
o	Removes the album from the collection and returns "Album {name} has been removed."  
o	If the album is published, return "Album has been published. It cannot be removed."  
o	If the album is not in the collection, return "Album {name} is not found."  

-	details()  
o	Returns the information of the band, with their albums, in this format:  
"Band {name}  
 {album details}  
 ...  
 {album details}  
"  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|song = Song("Running in the 90s", 3.45, False)<br>print(song.get_info())<br>album = Album("Initial D", song)<br>second_song = Song("Around the World", 2.34, False)<br>print(album.add_song(second_song))<br>print(album.details())<br>print(album.publish())<br>band = Band("Manuel")<br>print(band.add_album(album))<br>print(band.remove_album("Initial D"))<br>print(band.details()) |Running in the 90s - 3.45<br>Song Around the World has been added to the album Initial D.<br>Album Initial D<br>== Running in the 90s - 3.45<br>== Around the World - 2.34<br><br>Album Initial D has been published.<br>Band Manuel has added their newest album Initial D.<br>Album has been published. It cannot be removed.<br>Band Manuel<br>Album Initial D<br>== Running in the 90s - 3.45<br>== Around the World - 2.34<br>|






## **09.	Todo List -** [Solution](https://github.com/elenaborisova/Python-OOP/tree/main/02.%20Defining%20Classes%20-%20Exercise/todo_list_09/project)
You are tasked to create two classes: a Task class and a Section class. The Task class should receive a name (string), and a due_date (str) upon initialization. The Task also has two attributes: comments (empty list) and completed set to False by default.  
The Task class should also have five methods:  

-	change_name(new_name: str)  
o	Change the name of the task and return the new name.  
o	If the new name is the same as the current name, return "Name cannot be the same."  

-	change_due_date(new_date: str)  
o	Change the due date of the task and return the new date.  
o	If the new date is the same as the current date, return "Date cannot be the same."  

-	add_comment(comment: str)  
o	Add a comment to the task.  

-	edit_comment(comment_number: int, new_comment: str)  
o	If the comment_number is in the comments, change the comment and return all of the comments, separated by comma and space (", ")  
o	If the comment_number is not in the comments, return "Cannot find comment."  

-	details()  
o	Return the task's details in this format:  
"Name: {task_name} - Due Date: {due_date}"  
The Section class should receive a name (string) upon initialization. The Task also has one attributes: tasks (empty list)  

The Section class should also have four methods:  
-	add_task(new_task: Task)  
o	Add a new task to the collection. Return "Task {task details} is added to the section"  
o	If the task is in the collection, return "Task is already in the section {section_name}"  

-	complete_task(task_name: str)   
o	Change the task to completed. Return "Completed task {task_name}"  
o	If the task is not found, return "Could not find task with the name {task_name}"  

-	clean_section()  
o	Removes all of the completed tasks and returns "Cleared {amount of removed tasks} tasks."

-	view_section()  
o	Return information about the section and it's tasks in this format:  
    "Section {section_name}:  
     {details of the first task}  
     {details of the second task}  
     ...  
     {details of the n task}  
    "  

*Examples*

|       Test Code       |      Output       |
|-----------------------|-------------------|
|task = Task("Make bed", "27/05/2020")<br>print(task.change_name("Go to University"))<br>print(task.change_due_date("28.05.2020"))<br>task.add_comment("Don't forget laptop")<br>print(task.edit_comment(0, "Don't forget laptop and notebook"))<br>print(task.details())<br>section = Section("Daily tasks")<br>print(section.add_task(task))<br>second_task = Task("Make bed", "27/05/2020")<br>section.add_task(second_task)<br>print(section.clean_section())<br>print(section.view_section()) |Go to University<br>28.05.2020<br>Don't forget laptop and notebook<br>Name: Go to University - Due Date: 28.05.2020<br>Task Name: Go to University - Due Date: 28.05.2020 is added to the section<br>Cleared 0 tasks.<br>Section Daily tasks:<br>Name: Go to University - Due Date: 28.05.2020<br>Name: Make bed - Due Date: 27/05/2020    |




