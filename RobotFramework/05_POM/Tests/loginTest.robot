*** Settings ***
Resource    ../Pages/loginPage.robot
*** Test Cases ***
test login
    open website Adayroi
    click button DangNhap,DangKy
    type username    hainv
    type password    123456
    click button login