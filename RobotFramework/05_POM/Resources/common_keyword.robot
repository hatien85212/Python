*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To Login Page and Maximize
	Open Browser    ${LOGIN URL}    ${BROWSER}
	Maximize Browser Window
    Set Selenium Speed    ${DELAY}

wait and input text
    [Arguments]    ${locator}    ${txt_value}
    Wait Until Element Is Visible     ${locator}
    Input Text    ${locator}    ${txt_value}

wait and click element
    [Arguments]    ${locator}
     Wait Until Element Is Visible     ${locator}
     Click Element    ${locator}


Check Element Visible
    [Arguments]    ${locator}
    ${present}=    Run Keyword And Return Status    Element Should Be Visible       ${locator}    10s
    [Return]    ${present}