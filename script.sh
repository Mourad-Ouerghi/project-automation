#!/bin/sh

read -p "Enter the name of the project : " projectName
cd "D:/personal/self-dev/projects"
mkdir ${projectName}
cd ${projectName}
git init