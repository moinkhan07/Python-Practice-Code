'''
    step1: python -m venv(This is folder name) myenv(new Environment name)
    step2: source myenv/bin/activate  (THIS IS FOR MACBOOK)
           myenv\Scripts\activate.bat (THIS IS FOR WINDOWS)
           now install anything in new python in myenv folder this will be new python environment  
    step3: exit() exit from the virtual environment
    step4: deactivate the python
'''

'''
    we use this to tell another developer that in this projects this packages are needed
           pip freeze will show us the packages that are install on that environment 
    Step1: pip freeze > requirement.txt (IT WILL COPY AND PASTE ALL PACKAGES THAT ARE INSTALL ON THAT ENIVORNMENT IN THE requiremnet.txt)
    step2: pip install -r requirement.txt (IT WILL INSTALL ALL THE PACKAGES THAT ARE IN THE requiremnet.txt TO YOUR ENVIORNMENT)
'''