from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Anindita Sahoo"
DESCRIPTION = "This is a first project"
PACKAGES = ["housing"] ### the folder name which we created, as here we have only one folder, we have included only one
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return the list of requirement mentioned in requirements.txt file
    
    return : This function is going to return a list which will contain name of libraries mentioned in the requirements.txt file.
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        #return requirement_file.readlines().pop("-e .")
        #return requirement_file.readlines().remove("-e .")
        #return requirement_file.readlines()
        requirement_list = requirement_file.readlines()
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list



setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages= find_packages(),## we also can write find_packages() or PACKAGES
    ### this find_package is going to return the list of name of the folder where this __init__ is present.
    install_requires = get_requirements_list()
    ### along with the packages we need of external libraries to be installed hence install_requires used.
)
