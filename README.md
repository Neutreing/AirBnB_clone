# MY AIRBNB CLONE: Command Interpreter project

This project is the first step towards building my first full web application: AirBnB clone. It is a very important step because what is being built here is going to be used in other projects: HTML/CSS templating, database storage, API, front-end integration...


# The tasks in this projects would help me to::
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

# The aim of this project is to write a command interpreter to manage my AirBnB objects. The command interpreter would:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object.


# How to start the command interpreter
$ ./console.py  #console.py is the name of the file for the interpreter
(hbnh)

# How to use it
Interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$



Non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
# Examples
