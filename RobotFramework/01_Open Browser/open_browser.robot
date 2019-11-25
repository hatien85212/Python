*** Settings ***
Library  Selenium2Library

*** Test Cases ***
Testcase1
    Open Browser    http://robotframework.org    chrome
    Close Browser
    Log to console    Complete A
