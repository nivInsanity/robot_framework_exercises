*** Settings ***
Documentation    Explain what these tests do here
Resource    ../Resources/FrontOfficeApp.robot
Resource    ../Resources/CommonWeb.robot
Test Setup    Begin Web Test
Test Teardown    End Web Test

# robot -d results tests/Front_Office.robot

*** Variables ***
${BROWSER} =    edge
${URL} =    https://automationplayground.com/front-office/

*** Test Cases ***
Should be able to access "Team" page
    [Documentation]    Test number 1
    [Tags]    test1
    log    Executing test number 1
    sleep    4s

"Team" page should match requirements
    [Documentation]    Test number 2
    [Tags]    test2
    log    Executing test number 1
    sleep    4s