*** Settings ***
Resource    ../Resources/common_keyword.robot

*** Variables ***
${url}    https://www.adayroi.com/
${btn_DangNhap_DangKy}      Class:header-username
${txt_name}    id:j_username
${txt_pass}    id=j_password
${btn_login}    css=.btn.btn-primary.btn-block.js-login-btn

*** Keywords ***
open website Adayroi
    Open Browser    ${url}    chrome

click button DangNhap,DangKy
    wait and click element    ${btn_DangNhap_DangKy}

type username
    [Arguments]    ${txt_value}
    wait and input text    ${txt_name}     ${txt_value}

type password
    [Arguments]    ${txt_value}
    wait and input text    ${txt_pass}     ${txt_value}

click button login
    wait and click element    ${btn_login}