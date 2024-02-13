DESCRIPTION OF THE PROJECT

The goal of the project is to clone an airbnb website,  The console serves as a command interpreter, facilitating the management of object abstraction and storage. For more detailed information about the project's background, refer to the Wiki. The console's functionalities include creating new objects, retrieving objects from files, performing operations on objects, and deleting objects.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine


Table of Contents
- [Introduction](#introduction)
- [Environment](#environment)
- [Installation](#installation)
- [Testing](#testing)
- [Usage](#usage)
- [Authors](#authors)

INTRODUCTION 

# Team project to build a clone of [AirBnB](https://www.airbnb.com).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project, visit the [Wiki](link_to_wiki).

The console will perform the following tasks:
- create a new object
- retrieve an object from a file
- do operations on objects
- destroy an object


## Environment

The project was developed using the following technologies and tools:

- **Programming Language:** Python 3.8.3
- **Terminal:** Suite CRM
- **IDEs/Editors:**
  - VIM 8.1.2269
  - VSCode 1.6.1
  - Atom 1.58.0
- **Version Control System:** Git 2.25.1
- **Operating System:** Ubuntu 20.04 LTS


Installation

## Installation

To get started with the AirBnB clone project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/
    ```

2. Change to the AirBnB directory:

    ```sh
    cd AirBnB_clone
    ```

3. Run the command:

    ```sh
    ./console.py
    ```

This will launch the console for managing AirBnB objects.



## Testing

All tests are defined in the `tests` folder.

### Modules:

To see the documentation for a module:

```sh
python3 -c 'print(__import__("my_module").__doc__)'

To see the documentation for a class:

python3 -c 'print(__import__("my_module").MyClass.__doc__)'


Functions (inside and outside a class):
To see the documentation for a function:
sh

python3 -c 'print(__import__("my_module").my_function.__doc__)'

python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

Python Unit Tests:
* Module: unittest module
* File Extension: .py
* Files and Folders Naming Convention: Start with test_
* Organization: For example, for models/base.py, unit tests are in tests/test_models/test_base.pyExecution Command


EXECUTE COMAND

Discover all tests 
python3 -m unit-test discover tests


Discover  specific. Test file:
python3 -m unittest tests/test_models/test_base.py


INTERACTIVE MODE





