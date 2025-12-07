#!/bin/bash
# ./copy_dev_to_main_readme.sh
# "$(find . -type f -name "copy_dev_to_main_readme.sh")"


shopt -s expand_aliases
source ~/.bash_profile

START_TIME="$(date +%s.%N)"
file_absolute_path="$(readlink -f "$0")"
project_root_path="$(dirname "$(dirname "$file_absolute_path")")"
echo "$file_absolute_path"

git checkout dev
dev_README="$(cat README.md)"

git checkout main
echo "$dev_README" > README.md
push_main

git checkout dev

END_TIME="$(date +%s.%N)"
ELAPSED_TIME="$(echo "$END_TIME - $START_TIME" | bc)"
echo "実行時間:""$ELAPSED_TIME""s"
