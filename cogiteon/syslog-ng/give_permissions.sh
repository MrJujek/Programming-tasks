#!/bin/bash

group="logi"
user="logi"
folders=("wazuh" "fortigate" "wifi")

for folder in "${folders[@]}"; do
        path="/var/log/$folder"
        sudo chgrp -R $group $path
        sudo chown -R $user $path
        sudo chmod -R g+rx $path
done