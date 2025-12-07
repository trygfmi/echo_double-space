# ./start_update-readme.sh "testtest"
# "$(find . -type f -maxdepth 2 -name "start_update-readme.sh")" "testtest"


argument_number=${#@}
if [ $argument_number != 2 ]; then
    echo "引数はコミットメッセージとブランチ名の2つにしてください"
    exit 1
fi

shopt -s expand_aliases
source ~/.bash_profile

START_TIME=$(date +%s.%N)

commit_message="${1:-"auto update"}"
branch="${2:-"dev"}"
file_absolute_path="$(readlink -f "$0")"
directory_path="$(dirname "$file_absolute_path")"
echo "$directory_path"
cd "$directory_path"

python "$directory_path""/get-code-editor-value.py"
"$directory_path""/""update_readme.sh" "$commit_message" "$branch"

END_TIME=$(date +%s.%N)
ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
echo "実行時間:""$ELAPSED_TIME""s"
