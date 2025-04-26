# putting all imports into one place so have only one import file where we define imports and global vars
*** Settings ***
# import libraries that everything is going to use
Library     py-path.py
Library     Collections
Library     OperatingSystem

# import code
Library     get_objects.py
Resource    keywords.robot