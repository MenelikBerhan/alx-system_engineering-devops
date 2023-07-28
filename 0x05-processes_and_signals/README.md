# __0x05-processes_and_signals__

## 0-what-is-my-pid

a Bash script that displays its own PID.

## 1-list_your_processes

a Bash script that displays a list of currently running processes.

- Shows all processes, for all users, including those which might not have a TTY
- Displays in a user-oriented format
- Shows process hierarchy

## 2-show_your_bash_pid

a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

- Doesn't use `pgrep`

## 3-show_your_bash_pid_made_easy

a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

- Doesn't use `ps`

## 4-to_infinity_and_beyond

a Bash script that displays `To infinity and beyond` indefinitely.

- In between each iteration of the loop, adds a `sleep 2`

## 5-dont_stop_me_now

a Bash script that stops `4-to_infinity_and_beyond` process.

- Uses `kill`

## 6-stop_me_if_you_can

a Bash script that stops `4-to_infinity_and_beyond` process.

- Doesn't use `kill` or `killall`

## 7-highlander

a Bash script that displays:

- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

## 8-beheaded_process

a Bash script that kills the process `7-highlander`.

## 100-process_and_pid_file

a Bash script that:

- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a `SIGTERM` signal
- Displays `Y U no love me?!` when receiving a `SIGINT` signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal

## 101-manage_my_process, manage_my_process

`manage_my_process` Bash script that:

- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for `2` seconds

Bash (init) script `101-manage_my_process` that manages `manage_my_process`.

- When passing the argument `start`:
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process started`
- When passing the argument `stop`:
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Displays `manage_my_process stopped`
- When passing the argument `restart`
  - Stops `manage_my_process`
  - Deletes the file `/var/run/my_process.pid`
  - Starts `manage_my_process`
  - Creates a file containing its PID in `/var/run/my_process.pid`
  - Displays `manage_my_process restarted`
- Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed

## 102-zombie.c

a C program that creates 5 zombie processes.

- For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
- When the code is done creating the parent process and the zombies, it uses the function bellow

```c
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
