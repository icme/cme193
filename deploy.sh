#!/usr/bin/env bash

git checkout master

ROOTDIR=$(pwd)
WEBDIR=./web

cd $WEBDIR
couscous deploy

cd $ROOTDIR
git checkout gh-pages
git fetch origin
git rebase origin/gh-pages

git checkout master nb
git stash
git merge stash
git stash drop
git add nb
git commit -am "sync nb/ root"

git push origin

git checkout master

