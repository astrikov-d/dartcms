#!/bin/bash

# AUTHOR: Dmitry Astrikov <astrikov.d@gmail.com> www.astrikov.ru
#
# DarCMS Installation script.

cd ..
project_root=$(pwd)

echo "Project root is $project_root"

echo "Please type the name of your project:"

read project_name

echo "Creating virtual envinronment.."
virtualenv --no-site-packages --prompt="($project_name)" venv
echo "Success.."

echo "Installing dependencies.."
source venv/bin/activate
pip install -r ./install/dependencies.txt
echo "Success.."

echo "Installing models.."
python manage.py migrate
echo "Sucsess.."

echo "Loading fixtures"
python manage.py loaddata app/fixtures/setup.yaml
echo "Success"

read -p "Initial install is done. Do you want to install nodejs packages for admin app? (y/n)" -n 1 -r
echo 
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Installing node packages.."
    cd $project_root/app/static/adm/assets/bootstrap
    npm install
    echo "Success.."
    cd $project_root/app/static/adm/css
    npm install
    echo "Success.."
fi

echo "Setup is done. Don't forget to tune your settings.py file."
