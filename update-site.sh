#!/bin/bash

echo "did it worked"
sleep 2
echo "the button clicked is $1"
sleep 3
echo "just woke up bro"
sleep 1
cd /home/travis/Documents/coding-projects
pwd
sleep 2
echo "script done"
# path="/home/$1"

# echo "Updating $1"


# cd $path
# echo "updating npm packages"
# npm install
# cd $path
# echo "pulling repo"
# git pull
# cd $path
# echo "Updating browser list"
# npx update-browserslist-db@latest -y
# cd $path
# echo "Creating production build"
# npm run build
# echo "Done, thanks for playing!"