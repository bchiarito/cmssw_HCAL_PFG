#! /bin/bash
cat `ls -1 $1/* | grep 'out_.*.txt'`
