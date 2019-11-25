*** Settings ***
Documentation  If have the same name from Resource, need to mention the reference resource.method
Library    SeleniumLibrary
Variables   ../Resources/settings.py
Variables  ../Resources/variables.py

*** Keywords ***
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