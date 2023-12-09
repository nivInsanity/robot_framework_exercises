*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${PORTFOLIO_HEADER_LABEL} =  css:#portfolio > div > div:nth-child(1) > div > h2

*** Keywords ***
Verify Page Loaded
    Wait Until Page Contains Element    ${PORTFOLIO_HEADER_LABEL}