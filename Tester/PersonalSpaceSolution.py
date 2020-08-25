# Program to generate solution files for the PersonalSpace homework assignment

import ProgramTester as PT
import os, shutil
import random
    
def main():
    # Create a ProgramTester object
    pt = PT.ProgramTester("PersonalSpace")
    # Build the program (the solution)
    pt.build_program()
    
    # Create the solution directory
    try:
        os.mkdir("solution")
    except:
        shutil.rmtree("solution")
        os.mkdir("solution")
    
    # Define what command line arguments we want to test with
    arguments = []
    for i in range(1, 10): # Test each individually
        arguments.append("{}".format(i))
    arguments.append("1 2 3 4 5 6 7 8 9") # Test all at once
    # Test multiple of the same numbers at once
    s = ""
    for i in range(1, 10):
        for j in range(3):
            s+="{} ".format(i)
    arguments.append(s)
    # Test all the numbers in a random order
    n = [i for i in range(1, 10)]
    random.shuffle(n)
    s = ""
    for i in n:
        s += "{} ".format(i)
    arguments.append(s)
    # Test with 100 numbers all chosen randomly
    s = ""
    for i in range(1, 101):
        s += "{} ".format(int(random.uniform(1, 9)))
    arguments.append(s)
    # Test with inputs that are not recognized
    arguments.append("100")
    arguments.append("1 2 3 43")
    s = ""
    for i in range(1, 101):
        s += "{} ".format(int(random.uniform(1, 100)))
    arguments.append(s)
    
    # Generate the solution files
    for i, a in enumerate(arguments):
        # Run the program with the given arguments
        out = pt.execute_program(a)
        f = open("{}/output_{}.txt".format(pt.solution_dir, i), 'w')
        f.write("# Command arguments: {}\n# Solution:\n".format(a))
        for l in out:
            f.write("{}\n".format(l))
        f.close()
    # Write the command line arguments to a file for reproducability
    f = open("{}/command_arguments.txt".format(pt.solution_dir, i), 'w')
    s = ""
    for i, a in enumerate(arguments):
        s += "[args for output_{}.txt] {}\n".format(i, a)
    f.write(s)
    f.close()

    
if __name__ == "__main__":
    main() 