*** Settings ***
Resource    ./PO/Landing.robot
Resource    ./PO/Team.robot
Resource    ./PO/TopNav.robot
Resource    ./PO/Portfolio.robot
*** Variables ***


*** Keywords ***
Go To Landing Page
    Landing.Navigate To
    Landing.Verify Page Loaded

Go To "Team" Page
    TopNav.Select "Team" Page
    Team.Verify Page Loaded

Go To "Portfolio" Page
    TopNav.Select "Portfolio" Page
    Portfolio.Verify Page Loaded

Validate "Team" Page
    Team.Validate Page Contents