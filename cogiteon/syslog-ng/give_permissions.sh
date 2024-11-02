#!/bin/bash

group="logi"
user="logi"
folders=("wazuh" "fortigate" "wifi" "dx200" "sx1" "sx2" "sx3" "veeam")

for folder in "${folders[@]}"; do
        path="/var/log/$folder"
        sudo chgrp -R $group $path
        sudo chown -R $user $path
        sudo chmod -R g+rx $path
done