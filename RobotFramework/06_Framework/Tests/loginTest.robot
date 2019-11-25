*** Settings ***
Resource  resource.robot
Test Setup  Open Browser    ${LOGIN URL}    ${BROWSER}
Test Teardown  Close browser

*** Test Cases ***
Valid Login  [Template]  Login Success
  ${VALID USER}    ${VALID PASSWORD}
Valid Login Gherkin
[Documentation] Gherkin format is used in this test case
	Given Browser is opened to login page
	When User "tien.dao@terralogic.com" logs in with password "1Ylcotlmi"
	Then Welcome page should be open
Valid Login Gherkin - Test
[Documentation] Gherkin format is used in this test case
	Given Browser is opened to login page
	When Login Success "tien.dao@terralogic.com" "1Ylcotlmi"
	Then Welcome page should be open
*** Keywords ***
Login Success
    [Arguments]    ${username}    ${password}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Input Username    ${username}
    Input Pass    ${password}
    Click Button    signin
	Welcome page should be open
		
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Pass    ${password}
    Submit Credentials
    Comment Login Should Have Failed

Browser is opened to login page
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

User "${username}" logs in with password "${password}"
    Input Username    ${username}
    Input Pass    ${password}
    Click Button    signin
Welcome page should be open
	Log To Console    Login is successful
    Wait Until Element Contains    //*[@class='welcome']    Welcome
    Get Window Titles

	
	
