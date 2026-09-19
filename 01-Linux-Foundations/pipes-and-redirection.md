-- pipes, redirection and command compostions ----

[>] you can redircet output to somewhere else useing the > operator
like ls > files.txt, instead of listing content in the terminal, it puts the output contents into files.txt
[>] overwrites files though

[>>] operator: if you want to append a file you can use the >> operator, ls >> files.txt now appends the conent of files.txt with the ls

df : lisst file system disk space usage, lets say you do [df -h] to get disk information,  you could do df -h > disk_report.txt to write the output to a file called disk_report.txt

[|] pipes: pipes takes the output of the command on the left and passes it as an input to the command on the right

you can redirect errors with 2>
there are two types of output:
    - stdout -> normal output
    - stderr -> error output

you can redirect the errors with 2> , 2 represent s the standard error stream
some_command 2> errors.txt

this matters becase you can write scripts to do commands and write them to files: 
    df -h > disk_report.txt
    grep "ERROR" app.log > errors.txt
    grep "ERROR" app.log | wc -l
