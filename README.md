# ML_Regression
Here we are solving the Regression Problem.

# Software and Account Requirements:

1. [Github Account] (https://github.com/login)
2. [Heroku Account] (https://id.heroku.com/login or https://signup.heroku.com/)
3. [VSCode IDE] (https://code.visualstudio.com/download)
4. [Git Cli] (https://git-scm.com/downloads)
5. [Documentation](https://git-scm.com/docs/gittutorial)

### Create the conda envrironment 
```
conda create -p <env_name> python==3.7 -y
```
### Activate the virtual Environment:
```
conda activate venv/
```
### create the requirements.txt file
Write all the requirements inside the requirements.txt

### install the requirements.txt
```
pip install -r requirements.txt
```
### To add the files to the git
```
git add .
```
### To know the status of the git(like which file is updated)
```
git status
```
### To know the version of the git push
```
git log
```
### To update in the git the commands are:
```
git add .
git commit -m "message"
git push origin main
```
### To know the origin i.e. the URL (used during git clone url):
```
git remote -v
```
### To build the CI/CD pipeline we need 3 information from Heroku i.e.
```
1. HEROKU_EMAIL = anindita.sahoo2009@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-12thjune
```
### Create the docker image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase.
> During this process better open the docker desktop in yur system.
### To see the list of docker image in the system(command):
```
docker images
```
### To run the docker image
```
docker run -p 5000:5000 -e PORT=5000 IMAGE ID
```
### To check the running container
```
docker ps
```
### To stop the docker container
```
docker stop <CONTAINER ID>
```