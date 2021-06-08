# 0x0C. Python - Almost a circle

This project is a review of the following Python concepts:

+ Import
+ Exceptions
+ Class
+ Private attribute
+ Getter/Setter
+ Class method
+ Static method
+ Inheritance
+ Unittest
+ Read/Write file
+ args and kwargs
+ Serialization/Deserialization
+ JSON

## Resources


[args/kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)

[JSON encoder and decoder](https://docs.python.org/3/library/json.html)

[unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)

[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## File Structure
* [models](models)
  * [base.py](models/base.py) - Contains the base class `Base`
  * [rectangle.py](models/rectangle.py) - Contains the class `Rectangle`, a subclass of `Base`
  * [square.py](models/square.py) - Contains the class `Square`, a subclass of `Rectangle`
* [tests](tests)
  * [test_models](tests/test_models)
    * [test_base.py](tests/test_models/test_base.py) - Contains all tests pertaining to class `Base`
    * [test_rectangle.py](tests/test_models/test_rectangle.py) - Contains all tests pertaining to class `Rectangle`
    * [test_square.py](tests/test_models/test_square.py) - Contains all tests pertaining to class `Square`