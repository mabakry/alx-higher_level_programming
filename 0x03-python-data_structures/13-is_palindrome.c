#include "lists.h"

/**
 * list_len - calculate list length.
 * @head: list
 * Return: list length
 */

int list_len(listint_t **head)
{
	int n = 0;

	while (head && *head)
	{
		n++;
		*head = (*head)->next;
	}
	return (n);
}


/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list to be checked.
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	int new[list_len(head)], i = 0;
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
