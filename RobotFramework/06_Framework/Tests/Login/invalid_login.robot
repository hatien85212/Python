*** Settings ***
Documentation     A test suite containing tests related to invalid login.
...
...               These tests are data-driven by their nature. They use a single
...               keyword, specified with Test Template setting, that is called
...               with different arguments to cover different scenarios.
...
...               This suite also demonstrates using setups and teardowns in
...               different levels.
Resource  ../../Pages/loginPage.robot
Suite Setup       Open Browser To Login Page and Maximize
Suite Teardown    Close Browser
Test Setup        Go To Login Page
Test Template     Login With Invalid Credentials Should Fail

*** Test Cases ***               USERNAME        PASSWORD				Unmatch						Username							Password
Invalid Username                 invalid          ${VALID_PASSWORD}		NULL						Please enter a valid email address	NULL
Invalid Password                 ${VALID_USER}    invalid				Invalid Username/Password	NULL								NULL
Invalid Username And Password    invalid          whatever				
Empty Username                   ${EMPTY}         ${VALID_PASSWORD}
Empty Password                   ${VALID_USER}    ${EMPTY}
Empty Username And Password      ${EMPTY}         ${EMPTY}