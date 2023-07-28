#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - function to run infinute loop
 * Return: 0 Always
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
 * main - function to create five zombies process
 * Return: the result.
 */

int main(void)
{
	pid_t pd;
	char num = 0;

	while (num < 5)
	{
		pd = fork();

		if (pd > 0)
		{
			printf("Zombie process created, PID: %d\n", pd);
			sleep(1);
			num++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
