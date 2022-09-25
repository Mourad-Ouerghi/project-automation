# Project creation automation
The purpsoe of this project is to automate the repetitive task of initializing git in a local project then linking it to github using shell script and python.
### Pre-setup :
* go to your terminal and install selenium for python :

    `pip install selenium`
### Setup : 
    1.In the file script.sh line 6 change the path to where you want your projects to be created (accordingly to the line 12)
    2. In the file script.sh line 10 change the path of the script.py file
    3. if you're using chrome put the lines 12->15 in a comment
    4. open powershell and paste this command so you can run it from anywhere :
    New-Alias -Name create -Value path-of-script.sh 
### Usage :
* tap `create` in powershell  <br>
and let the magic happens
