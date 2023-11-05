#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list to be checked.
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int new[100], i = 0;
	listint_t *temp = *head, *cmp = *head;

	if (*head == NULL || head == NULL)
		return (1);

	while (temp)
	{
		new[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;

	while (cmp)
	{
		if (cmp->n != new[i])
			return (0);
		cmp = cmp->next;
		i--;
	}
	return (1);
}
