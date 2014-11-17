#cat
echo 'Text through stdin' | cat - has_content.txt
cat -s multiple_blanks.txt
cat multiple_blanks | tr -s '\n'


