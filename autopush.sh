#!/bin/bash

cd /home/ubuntu/hipda-simple-search
python3 gettitles.py

git add .
git commit -m 'update db'
git push origin master
git push gitee master
#git push mirror
