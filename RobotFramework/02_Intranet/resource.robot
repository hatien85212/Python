*** Settings ***
Library           Selenium2Library

*** Variables ***
${SERVER}         intranet.terralogic.com
${BROWSER}        ff
${DELAY}          0
${VALID USER}     tien.dao@terralogic.com
${VALID PASSWORD}    1Ylcotlmi
${LOGIN URL}      http://${SERVER}/
${WELCOME URL}    http://${SERVER}/index
${ERROR URL}      http://${SERVER}/error.html

*** Keywords ***
Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Pass
    [Arguments]    ${password}
    Input Password    password    ${password}