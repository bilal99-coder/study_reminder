challenges:
- could not import scheduler: find out that i have to intsall it by pip install scheduler 
- i had not that package installed in my computer, i did not know how to install it 
1 pip install -- user p a c k a g e n a m e
- did not worked i had to use a virtual environment to avoid getting that error
- /opt/homebrew/bin/python3.12 -m venv .venv this created a virtual environment directry called venv using the venv module preinstalled in python.
- to activate the virtual environment use source .venv/bin/activate
- in the beginning i did not know what i will design the reminder app like 
- I had great experience from the previuos assignment because i structured the deliverable as packages and created unit tests.
- importing all the modules to __init__.py did not worked in the sense that i dont have to explicitly import modules in each file.
- use pkgutil.get_data() instead of direct file openeing wit open() to avoid file paths problems ensuring full compatibility
- the naming convention in python seems to be a_b
- import sysconfig; print(sysconfig.get_paths()["purelib"])'
- although i imported the pythoin library schedule i had to restart my visual studio code ide multiple times before it came up. but i still could not use it becuase i was using the system python not the virtal envirniment python
- one of the biggest challenges was to figure out which environment i was using in a given time. This need to know the env i am using araises especially when you try to import a new module from pip.