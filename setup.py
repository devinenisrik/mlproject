from setuptools import find_packages,setup
from typing import List

hyp_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requiremets=[]
    with open(file_path) as file_obj:
        requiremets=file_obj.readlines() # this will give \n 
        requiremets=[req.replace('\n','') for req in requiremets]  #removing \n

        if hyp_e_dot in requiremets:
            requiremets.remove(hyp_e_dot)
    return requiremets


setup (
name='ml project',
version='0.0.1',
author='srik',
author_email='devinenis.34@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
## or we can use 
install_requires=get_requirements('requirements.txt')

)