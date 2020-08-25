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

You are to write a program to the following specifications:

1. Your program *shall* recieve an unknown number of command line arguments.
2. Your program *shall* print the appropriate statement from Mr. Phillip Jacobs (the host of "The Personal Space Show") for all command line arguments given an interger command line argument. E.g., if the command line argument is "1", print "One: Personal Space". E.g., if the command line argument is "7", print "Seven: Keep away from dat personal space". 
3. Your program *shall* print "N: Number not recognized" where N is some integer outside of [1, 9]. E.g., if the command line argument is "101", print "101: Number not recognized". 

You will be given the following code as a template:

'''c
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
'''