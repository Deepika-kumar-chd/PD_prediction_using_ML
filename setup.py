from setuptools import find_packages, setup


def get_requirements() -> list[str]:

    requirements_list = list[str] = []

    return requirements_list
 
setup(

    name = "pred",
    version = "0.0.1",
    author = "Deepika",
    author_email = "deepika.kumar.chd@gmail.com",
    packages = find_packages(), 
    install_requires = get_requirements()

)