# tools-of-curiosity-app
This repository hold everything for the Tools Of Curiosity game.

# Getting Started

## Set up Git LFS
* Install Git LFS from https://git-lfs.github.com
* Run `git lfs install` if you have never used git lfs on your machine before.
* Clone this repo. 
    * If you have already cloned this repo, go into it and run `git lfs pull`

## Set up Python
* Create a python virtualenv
    * `virtualenv --python=python3 venv`
* Install python requirements
    * `./venv/bin/pip install -r requirements.txt`

## Set up Heroku
* Install the Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli#download-and-install
* Set up your heroku instance
    * `heroku create`
* Follow setup instructions here: https://ankane.org/git-lfs-on-heroku

## Running Locally
* `source ./venv/bin/activate`
* `heroku local` 

## Deploying to Heroku
* `git push heroku main --no-verify`
