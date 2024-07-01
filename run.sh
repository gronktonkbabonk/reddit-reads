if [ ! -f .datafiles/oldposts.txt ]; then 
    echo "Looks like it's your first time running this tool. Setup started." 

    if [ -f .datafiles/* ]; then
        rm .datafiles/* 
    fi

    if [ -f .env ]; then 
        rm .env 
    fi

    touch ".datafiles/DO NOT EDIT ANYTHING IN HERE"
    touch ".datafiles/oldposts.txt"

    printf "%s" "Enter reddit username: " 
    read username
    printf "%s" "Enter reddit password: " 
    read -s password
    echo
    printf "%s" "Enter reddit bot client ID: "
    read clid
    printf "%s" "Enter reddit bot secret key: "
    read -s skey
    echo 

    cat << EOF >> .env
GRANT_TYPE = password
USERNAME = $username
PASSWORD = $password
CLIENT_ID = $clid
SECRET = $skey
EOF

else
    echo "running"
fi