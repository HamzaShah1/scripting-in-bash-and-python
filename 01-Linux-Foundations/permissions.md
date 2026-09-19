-- linux file permissions ------

-rwx-rwx-rwx
type - owner - group - others

first character tells you the type: 
- : regular file
d : directory

r - read
w - write
x - execute

this matter becayse  imagine you write a script:
touch backup.sh
then ./backup.sh

you might get permission denied: this is because creating a file doesnt necessarily make it executable
- you need to give yourself execute permission: chmod +x backup.sh

you can add / remove execute permission using chmod +x or chmod -x, you could also only give the owner execute permissions: chmod u+x script.sh
where:
u - owner
g = group
o = others

read / write permissions in file vs directory:
in a file:
r - read
w - write
x - execute

in a directory:
r - list directory contents
w - create / delete entries
x - enter/traverse directory

