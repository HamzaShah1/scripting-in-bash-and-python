-- reading and searching files -----

if youre working on an AWS server and someone says the application is not working, you wouldnt aautomatically change files; first of all youd look at the current files,
firstly youd look at the logs; for some evidence

cat : outputs contents of files - cat file.txt

head : imagine the log file has 100,000 lines, you dont want to dump the entire thing into your terminal. thats why you use head
head file.txt oly shows the beggining of the file
you can also sepcify how many lines you want to see using head -n [number]
head -n 5 file.txt shows only the first 5 lines of the file

tail : shows the end of the file, tail file.txt shows the end
tail -n 10 file.txt shows the last 10 lines in file.txt
tail -f : this one means follw the file, if there are new lines, it folls and prints them: tail -f application.log

less : for a large file, you can use less to navigate the file / scroll through it instead of dumping the entire contents

grep : use to serach or filter through text, grep "ERROR" application.log
you could pipe [|] grep into wc (used to count lines) to search for a certain keyword and see how many times it appears: grep "ERROR" application.log | wc -l

find : you use find to search for files (whereas grep is used to search within files), for example you could do find . -name "*.log" (find all files in the current directory that end in.log)

