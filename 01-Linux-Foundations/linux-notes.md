-- THE SHELL: ----

human writes ->  in terminal
terminal takes this and -> passes to shell
the shell translates this -> for the Operating System
the operating system -> allocates and uses computer resources

you can check your shell using [echo $SHELL]


----- some basic commands: ------

pwd : print working directory

whoami : prints user 

cd : change directory, use this to move into different directories

ls : list contents of current directory
ls -l : for more information
and ls -a : to see hidden files
could also do ls -la : combination of 2 above

uname -a :

echo $SHELL : check what shell youre using

--- CREATING, READING, MODIFYING, AND DELETING FILES: ----

mkdir - making directories
you can make nested repositories using mkdir 01-linux/notes
but if 01-linux didnt exist it wouldnt work
so you. can tell mkdir to make the necessary parent directory using the -p flag:
mkdir -p 01-linux/notes

touch : creating files 
(or if the file already exists, it updates its timestamps)

cp : copy files, create a duplicate

mv : moving and renaming files, moving the file to another filename is essentially renaming the file so thats why its the same command
you can also move it somewhere, or even just do [.] to move it to the current directory:
mv 01-linux/notes.md .

rm : deleting a file: rm notes.txt
and to delete a direcotry CONTAINGIN files: rm -r directory

