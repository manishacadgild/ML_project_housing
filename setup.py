from setuptools import setup
from typing import List

PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Manish Jha"
DESCRIPTION="This is my Housing prediction project"
PACKAGES=["housing"]
REQUIREMENTS_FILE="requirements.txt"
HYPEN_E_DOT='-e .'

def get_requirements_list()->List[str]:
    requirements=[]
    with open(REQUIREMENTS_FILE) as requirements_file:
        requirements=requirements_file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)