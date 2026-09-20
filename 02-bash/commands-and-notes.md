ping -c 1
we will use this command to ping a website 1 time. -c 1 means send 1 ICMP request instead of constantly pinging

exit codes:
every command in linxu produces an exit code, you can check the most recent one by doing echo $?
0 = success
non-0 = not success

-------- environment variables--------
export VAR_NAME = "abc" 
creates an environment variable that child proceses can inherit

VAR_NAME = "abc" 
creates a shell variable


-------- COMMAND SUBSTITUTION --------------
if you want to run a command in a command you use brackets (command_inside)
such as:
echo "$(date)"

-=--------cut----------

cut -d "," -f 2 "$1"
cut .csv by delimiter (-d) "," then return field 2 in the csv, $1 is the csv name




----------awk ---------
can use to splitylines into columns
inside awk you use $1 $2,3 .... to select fields/columns---- NOT LIKE BASH WHERE $1.. MEANS ARGUMENTS

awk print '{print $1}' file.txt
--> prints first field in each line 

by default awk considers whitespace to seperate columns " ".  insteasd you can tell awk to use something else as the field seperator with -F
awk -F "," '{print $2}' servers.csv

you can also add in conditions to the awk statement: awl ' condition {action}' file.txt
awk '$2 == "prod" {print $1}' servers.csv



-----------sed----------
sed stands for stream editor
most commonly used for find and replace: sed 's/FIND/REPLACE_WITH/'

ONLY CHANGES OUTPUT, DOESNT CHANGE FILE: TO ACTUALLY MODIFY THE FILE YOU DO -i
sed -i 's/prod/PROD' servers.csv
s/ is replace the FIRST occurance on every line
adding a: /g at the end. means replace every occurance on the line

you can use sed to delete files too: sed '/ERROR/d' app.log
in order to actually change the file you should use -i


-----------xargs----------
lets you take the output of one command and use it as an argument in another:
find . -name "*.log" | xargs wc -l



----------------ERROR HANDLING----------------------------
set -e
use this to exit script when a command fails

set -u
use this to stop if there is an unset variable, if a variable isnt set in a script (for example something important like an environment variable, then this will give an error instead of continuing)
normallly if you dont set a variable; bash will just give you an empty value for that variable, but with -u it will give an error if its unset


set -o pipefail
if you have a pipeline of commands command1 | command2 | command3
BASH cares about the exit status of the last command, so if you have false | echo "hello" : then the exit status will be successful
with set -o pipefail; if any one of the commands fails then the pipeline fails


commonly people put:
set -euo pipefail
which stands for the 3 commands together: set -e, set -u, and set -o pipefail. you can just combine it into one
meaning: stop if a command fails, catch unset variables, and catch faliures within pipelines



