*** Settings ***
Resource  ../Resources/Resource.robot

*** Test Cases ***
Login Success
[Documentation] Test
	Login Success
	[Teardown]  Close browser
	
