#!/bin/bash
for i in `seq 10 12`;
do
	python2 converteCSV.py "2016-"$i".pdf"
done