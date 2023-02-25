#!/bin/bash

repo_name=$(git config --get remote.origin.url | sed 's/.*\///;s/\.git$//')

git add .

git commit -m "Automatic commit by $USER at $(date)"

git push