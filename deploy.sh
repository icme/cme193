#!/usr/bin/env bash

git checkout master

ROOTDIR=$(pwd)
WEBDIR=./web

cd $WEBDIR
couscous deploy



if [[ $1 == "refresh" ]]; then
	echo "running REFRESH on nb/"
	cd $ROOTDIR
	git checkout gh-pages
	git fetch origin
	git rebase origin/gh-pages

	rm -rf nb
	git commit -am "full refresh"
	git checkout master nb
	git stash
	git merge stash
	git add nb
	git checkout master nb
	git add nb
	git push
	git stash drop

	git checkout master
fi



