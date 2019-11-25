*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource  ../../Pages/loginPage.robot

*** Test Cases ***
Login Success
    ${res}=  Login Success
    Log  ${res}
	[Teardown]  Close browser

Test case2
    Create Folder A  C:\\RF

# Keywords below used by higher level tests. Notice how given/when/then/and
# prefixes can be dropped. And this is a comment.