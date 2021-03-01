## Python OOP Exam 16 August 2020 – System Split

*You have been given the task to gather statistics about The System. The System is a network of components, connected to build something which functions logically, but you don’t need to know that. You need to build a program which processes statistics about The System.*


###### Structure (Problem 1) and Functionality (Problem 2)  
Our first task is to implement the structure and functionality of all the classes (properties, methods, inheritance, etc.)  

**1.	Class Software**  
In the file software.py implement the Software class:  
*Structure*  
The class should have the following attributes:  
•	name - string  
•	type - string ("Express" or "Light")  
•	capacity_consumption - int  
•	memory_consumption - int  
*Methods*  
\_\_init\_\_(name:str, type:str, capacity_consumption:int, memory_consmption:int)  
Set the attributes to the provided values  
*Note: Feel free to add any additional methods that might help you.*

**2.	Class LightSoftware**  
In the file light_software.py implement the LightSoftware class:  
•	The class should inherit from Software. Set the type to be "Light"  
•	An instance of the LightSoftware class has 50% more capacity_consumption than the given one  
•	An instance of the LightSoftware class has 50% less memory_consumption than the given one  

**3.	Class ExpressSoftware**  
In the file express_software.py implement the ExpressSoftware class:  
•	The class should inherit from Software. Set the type to be "Express"  
•	An instance of the ExpressSoftware class has two times more memory_consumption than the given one  

**4.	Class Hardware**  
In the file hardware.py implement the Hardware class:  
*Structure*  
The class should have the following attributes:  
•	name - string  
•	type - string ("Heavy" or "Power")  
•	capacity - int  
•	memory - int  
•	software_components - empty list upon initialization  
*Methods*  
\_\_init\_\_(name:str, type:str, capacity:int, memory:int)  
Set the attributes to the provided values  

• install(software:Software)  
If there is enough capacity and memory, add the software object to the software_components. Otherwise, raise Exception with message "Software cannot be installed"  

• uninstall(software:Software)  
Remove the software object from the software_components  
*Note: Feel free to add any additional methods that might help you.*

**5.	Class HeavyHardware**  
In the file heavy_hardware.py implement the HeavyHardware class:  
•	The class should inherit from Hardware. Set the type to be "Heavy"  
•	An instance of the HeavyHardware class has two times more capacity than the given one  
•	Its memory is 75% from the given memory upon initialization  

**6.	Class PowerHardware**  
In the file power_hardware.py implement the PowerHardware class:  
•	The class should inherit from Hardware. Set the type to be "Power"  
•	Its capacity is 25% from the given capacity upon initialization  
•	An instance of the PowerHardware class has 75% more memory than the given one  

**7.	Class System**  
The System class is where all the logic of the task will be implemented  
The class should have the following protected attributes:  
•	\_hardware - list storing all the hardware  
•	\_software - list storing all the software  
*Methods*  
All described methods below should be static!  
- register_power_hardware(name:str, capacity:int, memory:int)  
Create a PowerHardware instance and add it to the hardware list  
- register_heavy_hardware(name:str, capacity:int, memory:int)  
Create a HeavyHardware instance and add it to the hardware list  
- register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int)  
•	If the hardware with the given name does NOT exist, return a message "Hardware does not exist"  
•	Otherwise, create an ExpressSoftware instance, install it on the hardware (if possible) and add it to the software list (if installed successfully)  
•	If the installation is not possible return the message of the raised Exception  
register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int)  
•	If the hardware with the given name does NOT exist, return a message "Hardware does not exist"  
•	Otherwise, create a LightSoftware instance, install it on the hardware (if possible) and add it to the software list (if installed successfully)  
•	If the installation is not possible return the message of the raised Exception  
release_software_component(hardware_name:str, software_name:str)  
•	If both components exist on the system, uninstall the software from the given hardware  
•	Otherwise, return a message "Some of the components do not exist"  
- analyze()  
Return the following information (as a string). The total memory and capacity used is calculated of all hardware components in the system:  
System Analysis  
Hardware Components: {count of hardware components}  
Software Components: {count of software components}   
Total Operational Memory: {total used memory} / {total memory}  
Total Capacity Taken: {total used space} / {total capacity}  
system_split()  
Return the following information (as a string) for each hardware component:  
Hardware Component - {component name}  
Express Software Components: {number of the installed express software components}  
Light Software Components: {number of the installed light software components}  
Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}  
Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}  
Type: {type}  
Software Components: {names of all software components separated by ', '} (or 'None' if no software components)  

*Note: Feel free to add any additional methods that might help you.*

###### Unit Testing (Problem 3)  

In the test_hardware.py file create tests for the Hardware class.

               
*Examples*

Test code:  
    
        System.register_power_hardware("HDD", 200, 200)  
        System.register_heavy_hardware("SSD", 400, 400)  
        print(System.analyze())  
        System.register_light_software("HDD", "Test", 0, 10)  
        print(System.register_express_software("HDD", "Test2", 100, 100))  
        System.register_express_software("HDD", "Test3", 50, 100)  
        System.register_light_software("SSD", "Windows", 20, 50)  
        System.register_express_software("SSD", "Linux", 50, 100)  
        System.register_light_software("SSD", "Unix", 20, 50)  
        print(System.analyze())  
        System.release_software_component("SSD", "Linux")  
        print(System.system_split())  
        
Output:  
        System Analysis  
        Hardware Components: 2  
        Software Components: 0  
        Total Operational Memory: 0 / 650  
        Total Capacity Taken: 0 / 850  
        Software cannot be installed  
        System Analysis  
        Hardware Components: 2  
        Software Components: 5  
        Total Operational Memory: 455 / 650  
        Total Capacity Taken: 160 / 850  
        Hardware Component - HDD  
        Express Software Components: 1  
        Light Software Components: 1  
        Memory Usage: 205 / 350  
        Capacity Usage: 50 / 50  
        Type: Power  
        Software Components: Test, Test3Hardware Component - SSD  
        Express Software Components: 0  
        Light Software Components: 2  
        Memory Usage: 50 / 300  
        Capacity Usage: 60 / 800  
        Type: Heavy  
        Software Components: Windows, Unix  



