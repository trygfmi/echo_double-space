# ./update_readme.sh commit_message
# "$(find . -type f -maxdepth 2 -name "update_readme.sh")"


shopt -s expand_aliases
source ~/.bash_profile

commit_message="$1"
branch="$2"
file_absolute_path="$(readlink -f "$0")"
project_root_directory="$(dirname "$(dirname "$file_absolute_path")")"

cd "$project_root_directory"
convert_markdown_string

git add README.md
git commit -m "$commit_message"
git push origin "$branch"
