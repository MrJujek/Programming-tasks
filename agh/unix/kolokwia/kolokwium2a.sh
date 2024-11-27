#1
#!/bin/bash
while ((1)); do
    echo $(ps -aux | tail -n +2 | wc -l)
    sleep 3
done
#2
kill -SIGUSR1 1000
#3
export PATH=$PATH:$(pwd)
#4
#!/bin/bash

#5
ps -eo pid,%mem -e | awk -F" " '{if ($2 != "0.0") {print $1"\t"$2}}'