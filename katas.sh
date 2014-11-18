#cat
echo 'Text through stdin' | cat - has_content.txt
cat -s multiple_blanks.txt
cat multiple_blanks | tr -s '\n'

#find
find . \( -name 'file.txt' -o -name 'a.pdf' \)
find . -path '*tmp*' #find . -path 'tmp' 
find . -iregex ".*\.\(py\|pdf\)" # not work, why?
