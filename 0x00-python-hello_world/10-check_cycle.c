#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortois, *hare;

	tortois = hare = list;
	while (hare && hare->next)
	{
		tortois = tortois->next;
		hare = hare->next->next;

		if (tortois == hare)
			return (1);
	}
	return (0);
}
