#!/bin/sh

read -p "Enter the name of the project : " projectName
cd "D:/personal/self-dev/projects"
mkdir ${projectName}
cd ${projectName}
git init
cd "D:/personal/self-dev/scriptShell/projects/project-automation"
python script.py ${projectName}