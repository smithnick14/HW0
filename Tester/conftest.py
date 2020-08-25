import ProgramTester as PT
import pytest

# Build the program once before entering pytest
def pytest_configure():
    # Create a ProgramTester object
    pt = PT.ProgramTester("PersonalSpace")
    # Build the user's program 
    pt.build_program()