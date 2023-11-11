# Biker App

This test suite is related to the reporter software and tests all the automatable test scenarios.

1. AppiumLibrary: A popular tool for automating native and web app, used here to interact with the Reporter App.
2. YAML: For managing input data device in a structured way.
   To change the test input data, you can edit the yaml file in the following path: 
   biker_app/resources/base_config/data_device.yaml

**Installation:**

    git clone https://github.com/farzane-shafiee/biker_robotframework.git

    cd project
    
    create ENV and active it:

        for win: 
            python -m venv env

        for linux: 
            pip install virtualenv
            virtualenv --python=python3 venv
            source venv/bin/activate

    install dependencies:
        pip install -r requirements.txt
        
        
    run tests:
        robot -d biker_app/Results/ biker_app/tests/login/login.robot