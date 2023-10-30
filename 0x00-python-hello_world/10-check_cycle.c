#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to linked list header
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *R = list, *T = list;

	if (!list)
		return (0);

	while (R && T && R->next)
	{
		T = T->next;
		R = R->next->next;

		if (T == R)
			return (1);

	}
	return (0);
}
