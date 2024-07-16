#!/bin/bash

path="/home/$1"

echo "Updating $1"


cd $path
echo "updating npm packages"
npm install
cd $path
echo "pulling repo"
git pull
cd $path
echo "Updating browser list"
npx update-browserslist-db@latest -y
cd $path
echo "Creating production build"
npm run build
echo "Done, thanks for playing!"