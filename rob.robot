*** Settings ***
Library     DataDriver          MyWorkBook.xlsx
Test Template       TC1

*** Test Cases ***
TC1 ${Price} ${Product_Name}


*** Keywords ***

TC1
    [Arguments]         ${Product_Name}
    Log      ${Product_Name}