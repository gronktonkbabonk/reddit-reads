@echo off
if not exist ".datafiles\oldposts.txt" (
    echo Looks like it's your first time running this tool. Setup started.

    if exist ".datafiles\*" (
        del /q .datafiles\*
    )

    if exist ".env" (
        del .env
    )

    echo DO NOT EDIT ANYTHING IN HERE > ".datafiles\DO NOT EDIT ANYTHING IN HERE"
    type nul > ".datafiles\oldposts.txt"

    set /p username="Enter reddit username: "
    set /p password="Enter reddit password: "
    set /p clid="Enter reddit bot client ID: "
    set /p skey="Enter reddit bot secret key: "

    (
        echo GRANT_TYPE=password
        echo USERNAME=%username%
        echo PASSWORD=%password%
        echo CLIENT_ID=%clid%
        echo SECRET=%skey%
    ) >> .env
) else (
    echo running
)
