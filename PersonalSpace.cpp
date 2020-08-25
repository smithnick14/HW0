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
