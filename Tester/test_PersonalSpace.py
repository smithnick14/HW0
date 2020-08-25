# Program to test the Personal Space Homework assignments

import ProgramTester as PT
import pytest, os
    
def main():
    # Create a ProgramTester object
    pt = PT.ProgramTester("PersonalSpace")
    # Build the program
    pt.build_program()
    
    # Test the program with a given filename
    filename = "output_0.txt" # Change this to test another file
    pt.test_program(filename) 

# Parameterize the python test object with the 15 output files to test against    
@pytest.mark.parametrize('input', ["output_{}.txt".format(i) for i in range(1, 16)])    
def test_submission(input):
	# Get to the Tester directory
    #os.chdir("Tester")
    # Create a ProgramTester object
    pt = PT.ProgramTester("PersonalSpace")
    # Test the program with the program tester object
    assert pt.test_program(input)
    
if __name__ == "__main__":
    main() 