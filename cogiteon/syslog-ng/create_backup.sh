#!/bin/bash

today=$(date +%Y_%m_%d)
folders=("wazuh" "fortigate" "wifi" "macierz")

for folder in "${folders[@]}"; do
        sudo mkdir -p "/var/log/backups/$folder"

        for logs in "/var/log/$folder"/*/; do
                name=$(basename "$logs")

                if [ "$today" != "$name" ]; then
                        sudo tar -czvf "/var/log/backups/$folder/$name.tar.gz" "/var/log/$folder/$name"
                        sudo rm -r "/var/log/$folder/$name/"
                fi
        done
done