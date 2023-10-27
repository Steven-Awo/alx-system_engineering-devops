#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - A function that runs a while loop initinite.
 * Return: zero if infinite
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
 * main - A function that creates a five zombie processes.
 * Return: zero if infinite
 */

int main(void)

{
	pid_t pidd;
	char countts = 0;

	while (countts < 5)
	{
	pidd = fork();
	if (pidd > 0)
	{
	printf("Zombie process created, PID: %d\n", pidd);
	sleep(1);
	countts++;
	}
	else
	{
	exit(0);
	}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
