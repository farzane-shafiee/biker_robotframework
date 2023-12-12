Biker App
===============

Introduction
------------
[Robot Framework] is a generic open source automation framework for acceptance testing, acceptance test driven development (ATDD), and robotic process automation (RPA). It has simple plain text syntax and it can be extended easily with generic and custom libraries.

Robot Framework is operating system and application independent. It is implemented using Python which is also the primary language to extend it. The framework has a rich ecosystem around it consisting of various generic libraries and tools that are developed as separate projects.

[AppiumLibrary] is an appium testing library for Robot Framework. Library can be downloaded from PyPI.
It uses Appium to communicate with Android and iOS application similar to how Selenium WebDriver talks to web browser.

It is supporting Python 3.7+ (since Appium Python Client doesn't support Python 2.7 anymore)

Installation
------------
If you already have Python with pip installed, you can simply run:

    pip install robotframework
And for Appium Library the recommended installation method is using pip:

    pip install --upgrade robotframework-appiumlibrary

To Install latest source from the master branch, use this command: pip:

    pip install git+https://github.com/serhatbolsu/robotframework-appiumlibrary.git

Device Setup
------------
After installing the library, you still need to set up a simulator/emulator or real device to use in tests. iOS and Android have separate paths to follow, and those steps better explained in Appium Driver Setup Guide. Please follow the Driver-Specific Setup according to platform.
  
Usage
-----
    git clone https://git.snappfood.ir/testing/delivery-automation-test.git

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
        robot -d biker_app/Results/ biker_app/

Best Regards.