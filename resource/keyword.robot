*** Settings ***
Library      SeleniumLibrary
Variables    ../test bed/variables.py
Variables    ../test bed/elements.py
Resource     common_keyword.robot

*** Keywords ***

Open Browser To Application
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Set Selenium Speed    0.3
    Set Selenium Timeout    20

Login To Application
    [Arguments]    ${username}    ${password}
    Input Text        ${USERNAME}    ${username}
    Input Password    ${PASSWORD}    ${password}
    Click Button      ${LOGIN}

Open Device Config
    Click Element    ${DEVICE_CONFIG}
    Click Element    ${Click_new}
    Click Element    ${Click_Details}
    Input Text       ${INPUT_TEXT}    ${INPUT_CONFIG_NAME}
    Input Text       ${Description}    ${DESCRIPTION}
    Click Element    ${NEXT}

    Input Text       ${DEVICE_NAME}    ${DEVICE}
    Click Element    ${NEXT}

    Input Text       ${CHANGE_HOSTNAME}    ${HOST_NAME}
    Click Element    ${NEXT}

    Click Element    ${PUSH_CONFIG}
    Click Element    ${CLICK_OK}

    Click Element    ${CONFIG_NAME}
    Element Should Be Visible    ${CONFIG_SUCCESS_FINAL}
    Click Element    ${HIT_OK}

Open Config Jobs
    Click Element    ${CONFIG_JOBS}

Close Application
    Close Browser