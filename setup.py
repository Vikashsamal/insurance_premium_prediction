from setuptools import find_packages, setup
from typing import List

requirement_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."


def get_requirements() -> List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_name.replace("\n", '') for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list 


setup(name='Insurance',
      version='1.0',
      description='Insurance Project',
      author='Bikash Samal',
      author_email='vks.samal1992@gmail.com',
      packages=find_packages(),
      install_requirements=get_requirements()
      )
