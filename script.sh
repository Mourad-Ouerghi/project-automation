#!/bin/sh

    read -p "Enter the name of the project : " projectName
    read -p "Enter your github username : " github_username
    read -s -p "Enter your github password : " github_password
    cd "D:/personal/self-dev/projects"
    mkdir ${projectName}
    cd ${projectName}
    git init
    cd "D:/personal/self-dev/scriptShell/projects/project-automation"
    python script.py ${projectName} ${github_username} ${github_password}
    cd "D:/personal/self-dev/projects/${projectName}"
    touch "README.md"
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/Mourad-Ouerghi/${projectName}.git
    git push -u origin main

