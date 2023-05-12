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
	listint_t *p1, *p2;

	p1 = list;
	while (p1)
	{
		p2 = list;
		p1 = p1->next;

		while (p1 != p2->next)
		{
			if (p1 == p2)
				return (1);
			p2 = p2->next;
		}
	}
	return (0);
}
