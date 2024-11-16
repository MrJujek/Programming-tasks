#1
ls -R
#2
ls -a
#3
mkdir $HOME/c2 | touch $HOME/c2/text | man ls > $HOME/c2/text
#4
chmod 600 c2/text
chmod +t c2
#5
cp
#6
umask 0007
#7
find ~ -type f -exec du -h {} + | sort -rh | head -n 1
find ~ -maxdepth 2 -type f -exec du -h {} + | sort -rh | head -n 1