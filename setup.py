from setuptools import find_packages, setup
from typing import List

DASH_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if DASH_E_DOT in requirements:
            requirements.remove(DASH_E_DOT)

    return requirements

setup(
    name = "Email Spam Detection",
    version = "0.0.1",
    author = "Deb",
    packages = find_packages(),
    author_email = "debmalya.mondal@outlook.com",
    install_requires = get_requirements("requirements.txt")
)
