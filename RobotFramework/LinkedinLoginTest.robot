*** Settings ***
Library           Selenium2Library

*** Variables ***
${Username}       swtestacademy@gmail.com
${Password}       wrongpass
${Browser}        firefox
${SiteUrl}        http://www.linkedin.com
${DashboardTitle}    LinkedIn
${ExpectedWarningMessage}    Hmm, we don't recognize that email. Please try again.
${WarningMessage}    Login Failed!
${Delay}          5s
@{lst_List}       a1    a2    1    2    11    22
&{dic_Dic}        ID=1    Name=Tien    Age=30

*** Test Cases ***
Login Should Failed With Unregistered Mail Adress
    Open LinkedinPage
    sleep    ${Delay}
    Enter User Name
    Enter Wrong Password
    Click Login
    sleep    ${Delay}
    Assert Warning Message
    [Teardown]    Close Browser

test
    Open LinkedinPage
    Comment    sleep    ${Delay}

*** Keywords ***
Open LinkedinPage
    Open Browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Enter User Name
    Input Text    id=login-email    ${Username}

Enter Wrong Password
    Input Text    id=login-password    ${Password}

Click Login
    Click Button    css=[name=submit]

Check Title
    Title Should be    ${DashboardTitle}

Assert Warning Message
    Element Text Should Be    id=session_key-login-error    ${ExpectedWarningMessage}    ${WarningMessage}
