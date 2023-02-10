from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Shubham Panchal"
DESCRIPTION = "This project aims to predict housing prices"
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()-> List[str]:
    """
    This function is going to returen the list of requirements
    mentioned in requirements.txt file

    returns the list which contains the name of libraries mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    
setup(
    name = PROJECT_NAME,
    version=VERSION,
    author  = AUTHOR,
    description= DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)