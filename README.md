The LMS Tools are a collection of Python scripts useful when working with LMS.
I suggest using Python 3 but Python 2 should work as well for most scripts.

## lms-create-mod.py
Generate a skeleton for a module in the current working directory.

### Usage
```
lms-create-mod.py test_module
```

This will generate a class TestModule splitted into a `test_module.cpp` and
`test_module.h` file lying in the according `src` and `include` directories.
Appropriate `CMakeLists.txt` and `interface.cpp` are generated as well.

### Dependencies
- Python 2/3

## lms-create-lib.py
Generate a skeleton for a library in the current working directory.

### Usage
```
lms-create-lib.py test_lib
```

This will generate a `test_lib` directory and an example `CMakeLists.txt`.

### Dependencies
- Python 2/3

## lms-validate.py
Validate an XML or LCONF file or all such files in a given directory.

### Usage
```
lms-validate.py file.xml
lms-validate.py file.lconf
lms-validate.py my_folder
```

### Dependencies
- Python 2/3
- lxml (python3-lxml / python-lxml)
