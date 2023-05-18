#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to list
 *
 * Return: 0 if there it isn't a pilndrome, 1 if there it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *mid, *next;
	int isPalindrome;

	slow = fast = *head;
	prev = mid = NULL;
	isPalindrome = 1;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			isPalindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	while (prev != NULL)
	{
		next = prev->next;
		prev->next = slow;
		slow = prev;
		prev = next;
	}

	if (mid != NULL)
	{
		mid->next = slow;
		*head = mid;
	}
	else
	{
		*head = slow;
	}

	return (isPalindrome);
}
