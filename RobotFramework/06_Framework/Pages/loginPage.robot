*** Settings ***
Library           ../ExternalKeywords/UserKeywords.py
Resource          ../Resources/common_keyword.robot
Variables         ../Resources/settings.py
Variables         ../Resources/variables.py

*** Variables ***
${lbl_login}      xpath://strong[contains(.,'Login to Intranet DASHBOARD')]
${txt_name}       id:username
${txt_pass}       id:password
${btn_login}      id:signin
${lbl_welcome}    xpath://*[@class='welcome']
${err_miss_name}    xpath://input[@type='email']/following-sibling::small[@style='display: block;']
${err_miss_pass}    xpath://input[@type='password']/following-sibling::small[@style='display: block;']
${err_unmatching}    xpath://form/preceding-sibling::div[@style='display: block;']
${err_miss_name}    Company email can't be empty
${err_invalid_email}    Please enter a valid email address
${err_miss_pass}    The password is required and can't be empty
${err_invalid_pass}    The password must be more than 4 characters long
${err_invalid_pass}    The password must be more than 4 characters lon

*** Keywords ***
Open Browser To Login Page and Maximize
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Login

Input Username
    [Arguments]    ${username}
    Input Text    ${txt_name}    ${username}

Input Pass
    [Arguments]    ${password}
    Input Password    ${txt_pass}    ${password}

Submit Credentials
    Click Button    ${btn_login}

Login Success
    Open Browser To Login Page and Maximize
    Input Username    ${VALID_USER}
    Input Pass    ${VALID_PASSWORD}
    Submit Credentials
    ${title}=    Welcome page should be open
    Log    ${title}
    [Return]    True

Welcome page should be open
    Log To Console    Login is successful
    Wait Until Element Contains    ${lbl_welcome}    Welcome
    Get Window Titles
    ${title}=    Get Title
    Log    ${title}
    [Return]    ${title}

Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Pass    ${password}
    Submit Credentials

Login Should Have Failed
    Location Should Be    ${ERROR URL}
    Title Should Be    Error Page

Create Folder A
    [Arguments]    ${path}
    create_folder    ${path}
