#include <stdlib.h>
#include <stdio.h>
#include<unistd.h>

/**
 * infinite_while - infinite while loop
 * Return: always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates five zombie processes and hangs on while loop
 * Return: always 0
*/
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		exit(0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}
