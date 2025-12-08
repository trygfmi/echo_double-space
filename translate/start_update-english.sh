# bash $(find . -type f -maxdepth 2 -name "start_update-english.sh")
# "$(find . -type f -maxdepth 2 -name "start_update-english.sh")"


echo "start_update-english.shを実行します"


shopt -s expand_aliases
source ~/.bash_profile

START_TIME=$(date +%s.%N)

file_absolute_path="$(readlink -f "$0")"
project_root_path="$(dirname "$(dirname "$file_absolute_path")")"

python $(find "$project_root_path" -type f -maxdepth 2 -name "get_article_headings.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "get_article_sentences.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "get_translated_headings.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "get_translated_sentences.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "update_english_article_heading.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "update_english_article_other.py")
python $(find "$project_root_path" -type f -maxdepth 2 -name "update_english_article.py")

END_TIME=$(date +%s.%N)
ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
echo "実行時間:""$ELAPSED_TIME""s"
