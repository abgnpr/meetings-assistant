#! /bin/bash


if [[ $# -eq 1 ]]
then
    case $1 in

        -i|--install)

        ./generate_service.py
        sudo mv ./meetings-assistant.service /etc/systemd/system/.
        sudo systemctl daemon-reload
        sudo systemctl enable meetings-assistant
        sudo systemctl start meetings-assistant
        systemctl status meetings-assistant  --no-pager
        ;;

        -u|--uninstall)

        sudo systemctl stop meetings-assistant
        sudo systemctl disable meetings-assistant
        sudo rm -vf /etc/systemd/system/meetings-assistant.service
        sudo systemctl daemon-reload
        ;;
        
        -h|--help)
            printf "\nAvailable Options
        -i | --install\
          Installs Meetings Assistant service
        -u | --uninstall\
        Unsinstalls Meetings Assistant service
        -h | --help\
             Show help\n\n"

    esac
else
    printf "Invalid option(s), use '-h' to show help\n"
fi



