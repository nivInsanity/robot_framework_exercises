*** Settings ***
Documentation    Explain what these tests do here
Resource    ../Resources/FrontOfficeApp.robot
Resource    ../Resources/CommonWeb.robot
Test Setup    Begin Web Test
Test Teardown    End Web Test

# robot -d results tests/Front_Office.robot

*** Variables ***
${BROWSER} =    firefox
${URL} =    https://automationplayground.com/front-office/

*** Test Cases ***
Should be able to access "Team" page
    [Documentation]    Test number 1
    [Tags]    test1
    FrontOfficeApp.Go To Landing Page
    FrontOfficeApp.Go To "Team" Page

"Team" page should match requirements
    [Documentation]    Test number 2
    [Tags]    test2
    FrontOfficeApp.Go To Landing Page
    FrontOfficeApp.Go To "Team" Page
    FrontOfficeApp.Validate "Team" Page

Should be able to access "Portoflio" page
    [Documentation]    Test number 3
    [Tags]    test3
    FrontOfficeApp.Go To Landing Page
    FrontOfficeApp.Go To "Portfolio" Page