*** Settings ***
Documentation     This file is used to store setttings in the project.
...
...               Such as: browser, server, timeout
...				  To use this file: state Resource ../Resources/settings.robot
Library			  Selenium2Library

*** Variables  ***
${SERVER}         intranet.terralogic.com
${BROWSER}        ff
${DELAY}          0
${LOGIN_URL}      http://${SERVER}/
${WELCOME_URL}    http://${SERVER}/index
${ERROR_URL}      http://${SERVER}/error.html

${VALID_USER}     tien.dao@terralogic.com
${VALID_PASSWORD}    1Ylcotlmi

${txt_name}    id:username
${txt_pass}    id:password
${btn_login}   id:signin

${lbl_welcome}  xpath://*[@class='welcome']

*** Keywords ***
Login Success
	Open Browser To Login Page and Maximize
	Input Username  ${VALID_USER}
	Input Pass  ${VALID_PASSWORD}
	Submit Credentials
	Welcome page should be open
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Password    ${password}
    Submit Credentials
    Login Should Have Failed

	
Open Browser To Login Page and Maximize
	Open Browser    ${LOGIN_URL}    ${BROWSER}
	Maximize Browser Window
    Set Selenium Speed    ${DELAY}
	
Input Username
    [Arguments]    ${username}
    Input Text    ${txt_name}    ${username}

Input Pass
    [Arguments]    ${password}
    Input Password    ${txt_pass}    ${password}

Submit Credentials
    Click Button    ${btn_login}
	
Welcome page should be open
    Log To Console    Login is successful
    Wait Until Element Contains    ${lbl_welcome}    Welcome
    Get Window Titles
Login Should Have Failed
    Location Should Be    ${ERROR URL}
    Title Should Be    Error Page