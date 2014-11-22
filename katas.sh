#cat
echo 'Text through stdin' | cat - has_content.txt
cat -s multiple_blanks.txt
cat multiple_blanks | tr -s '\n'

//1-3天ycheng创建的perm为600的sh和rb文件，将他们的权限升为700，并ln到/usr/local/bin目录
#find
find . \( -name 'file.txt' -o -name 'a.pdf' \)
find . -path '*tmp*' #find . -path 'tmp' 
find . -iregex ".*\.\(py\|pdf\)$" # not work, why?
sudo find . -maxdepth 2 -type f ! -perm 644 -user ycheng -exec chown 644 {} \; #exec
find . \( -name "*haha" -prune \) -o \( -name "*qing.txt" \) # prune

#xargs
cat exp.txt | xargs -n 1 -I {} ./print.sh -p {} -l
find . -type f -name "*.bak" -print0 | xargs rm -rf



