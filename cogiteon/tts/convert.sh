#!/bin/bash

for file in ./*
do
	if [[ ( -f $file ) && ( $file == *.wav ) ]]; then
		filename=`echo $file | cut -c 3- | cut -d'.' -f1`
		ffmpeg -i $file -codec:a libmp3lame -q:a 2 "./converted/${filename}.mp3"
	fi
done
