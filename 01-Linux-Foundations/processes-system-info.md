-- Provcesses and system information ----

processses are running programs, whenm you run python app.py, the OS creates a process for that running python program, 
every process has a processs ID (PID)

ps: shows processes with PIDs
ps aux: shows extra information

you can combine ps with grep; ps aux | grep python
this is listing extra information about processes and searching for lines including python

top : continuously updating view of system activity, this can be useful for example if someone says the server is running sloiw: you can do top to investigate if one process is consuming exessive resources, press q to exit.

df : disk spaceusage of file system, df -h means human readable. you can run df -h from any directory, it doesnt matter, it shows how much disk space the file system is using.

du : directory usage, how much space is this directory using. the dfifference is df is how much the filesystem is using and du is how much space is this directory using
du -sh . how much space is this directory using. if you want to see how much file system usage a directory is using you would do du -sh . 

lsof -i :8080  : show which process is using port 8080

---- troubleshooting problem ----

if someone says their server is running slow; what steps would oyu take to troubleshoot:

1. ps aux : run this to check the current running processes in detail and get information about their memory and CPU usage
2. df -h : check if the filesystem is out of space, df -h chceks the file systems disk space usage
3. top : check the CPU and memory usage in real time, this would show the systems resources in realtime.