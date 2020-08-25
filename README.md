# ECE 275 Homework 0: The Personal Space Show!!

Welcome to ECE 275 and the Personal Space Show!!
<p align="center">
[![The Personal Space Show](https://img.youtube.com/vi/szjdoVR5EKs/0.jpg)](https://www.youtube.com/watch?v=szjdoVR5EKs)
</p>

> One: Personal Space
> 
> Two: Personal Space
>
> Three: Stay out of my personal space
> 
> Four: Keep away from my personal space
> 
> Five: Get outta dat personal space
> 
> Six: Stay away from my personal space
> 
> Seven: Keep away from dat personal space
> 
> Eight: Personal space
> 
> Nine: Personal space

Homework 0: "Personal Space" will test your ability to:

* Write and compile a simple C++ program
* Recieve and parse command line arguments (with help from the template)
* Perform basic control flow and loops (as discussed in ECE 175)

## Program Requirements
You are to write a program to the following specifications:

1. Your program *shall* recieve an unknown number of command line arguments.
2. Your program *shall* print the appropriate statement from Mr. Phillip Jacobs (the host of "The Personal Space Show") for all command line arguments given an interger command line argument. E.g., if the command line argument is "1", print "One: Personal Space". E.g., if the command line argument is "7", print "Seven: Keep away from dat personal space". 
3. Your program *shall* print "N: Number not recognized" where N is some integer outside of [1, 9]. E.g., if the command line argument is "101", print "101: Number not recognized". 

Below see two examples. Note that line starting with "#" should not be printed in your program and are there only to provide human and machine readable information. 

An example with one command line argument:

```
# Command arguments: 6
# Solution:
Welcome to the Personal Space Show!!
Six: Stay away from my personal space
```

Another example with multiple command line arguments:

```
# Command arguments: 1 2 3 4 5 6 7 8 9
# Solution:
Welcome to the Personal Space Show!!
One: Personal space
Two: Personal space
Three: Stay out of my personal space
Four: Keep away from my personal space
Five: Get outta dat personal space
Six: Stay away from my personal space
Seven: Keep away from dat personal space
Eight: Personal space
Nine: Personal space
```

## Writing Your Program
The github is populated with the following directory structure:

```
Homework0_PersonalSpace/
├── CMakeLists.txt
├── PersonalSpace.cpp
├── README.md
└── Tester
    ├── PersonalSpaceSolution.py
    ├── ProgramTester.py
    ├── conftest.py
    ├── solution
    │   ├── command_arguments.txt
    │   ├── output_0.txt
    │   ├── output_1.txt
    │   ├── output_10.txt
    │   ├── output_11.txt
    │   ├── output_12.txt
    │   ├── output_13.txt
    │   ├── output_14.txt
    │   ├── output_15.txt
    │   ├── output_2.txt
    │   ├── output_3.txt
    │   ├── output_4.txt
    │   ├── output_5.txt
    │   ├── output_6.txt
    │   ├── output_7.txt
    │   ├── output_8.txt
    │   └── output_9.txt
    └── test_PersonalSpace.py
```
You do NOT need to edit *anything* except for ```PersonalSpace.cpp```. The ```Tester``` directory houses the Python scripts to test the program (see below). There is an included CMakeLists.txt file - we will not learn CMake in this course but it's needed for the instructor to compile and run/test your code. Please do NOT edit the CMakeLists.txt file. Please, under no circumstances, should you edit the ```output_*.txt``` files. These were generated using the ```PersonalSpaceSolution.py``` file which the instructor has provided for transparency. 

You will be given the following code as a template:

```C++
/* Personal Space Show from Rick and Morty:
 *
 * The show is hosted by a man named Phillip Jacobs who is extremely concerned with his personal space
 * and takes it very seriously. At times he's paranoid that someone is close to him, even though he is
 * alone. After the intro he will direct the camera towards a projector and show slides saying "personal
 * space", and telling the viewers to stay out of his personal space. At the end of the show he removes
 * his own skin on live TV because he does not care to have it on his personal space.
 */

#include <iostream>
#include <stdlib.h>

int main(int argc, char **argv) {
	int i = 1;
	// Get the i th command line argument and convert to int
	int c = atoi(*(argv + i + 1));
	
	return 0; // Exit the program
}
```

Notice that there are constructs and functions used that have not been discussed yet - that is okay! I have provided you with the measn to get the i<sup>th</sup> command line argument from the list of command line arguments. The variable ```argc``` is short for "Argument Count" and represents the number of command line arguments passed to the program. The variable ```argv``` is short for "Argument Value" and is actually a pointer to a pointer of a charactor array. WOW :exploding_head: what does that mean!?!?! Well don't worry about that just now - we'll get there. You can get the i<sup>th</sup> command line argument by setting the variable ```i``` within the provided template code. The function ```atoi( ) ``` converts that charactor to an interger number - again, don't worry about that yet just try to have an idea of what's happening in the provided template. 

Command line arguments work as follows: 
If you have some program who's binary executable is named 'program' then you can execute the program using the ```./program``` command. In this example, ```argc``` would be one because the name of the executable is always the 0<sup>th</sup> command line argument. Therefore, ```*(argv)``` would be equal to "program". If the program was called as ```./program first second third``` then ```argc``` would be equal to 4 and, e.g., ```*(argv + 2)``` would equal "second". 

### Incrimental Buildup
Breaking this task into chunks, there are some main things you want to accomplish:

- [ ] Loop over the number of command lines given (using a ```for``` or ```while``` or ```do``` loop) and parse the i<sup>th</sup> command line argument. To test this, print it back out to the console
- [ ] Print the appropriate statement from Mr. Jacobs given the interger number. This can be accomplished using an ```if```-```else if```-```else``` statement or a ```switch``` statement. 

## Testing Your Program
To test your program, the instructor has written a custom Python-based testing framework which utilized pytest. You'll notice in ```Tester``` there are four Python3 scripts which will be used to test your program. When you create a pull request on GitHub, the program will execute ```pytest``` which will utilize the instructor's ```ProgramTester``` to test the output of your program against the solution for any given command line arguments. There are 16 test for this program which should run in under one second. If your output does not match the solution (except for whitespace. The tester disreguards linese that are completely whitespace), you will fail a test and the tester object will show exactly which lines are different. 