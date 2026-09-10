from setuptools import setup, find_packages
from typing import Tuple, List


HYPHEN_E_DOT= "-e ."

def get_requirements(filename: str) -> List[str]:
    """
    This function reads the requirements from a given file and returns them as a list of strings.
    """
    requirements = []
    with open(filename, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements =[ req.replace('\n', '')for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name= "CustomerChurn",
    version= "0.0.1",
    author="Sulav shrestha",
    author_email="sulavs84@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)