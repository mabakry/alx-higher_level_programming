#include "lists.h"

/**
 * add_node - add node at beginning of a list.
 * @head: list
 * @n: node to be added.
 * Return: address of the new node
 */

listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}


/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list to be checked.
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *cmp = NULL, *cmp_tmp = NULL;

	if (*head == NULL || temp->next == NULL)
		return (1);

	while (temp)
	{
		add_node(&cmp, temp->n);
		temp = temp->next;
	}

	cmp_tmp = cmp;
	while (*head)
	{
		if ((*head)->n != cmp_tmp->n)
		{
			free_listint(cmp);
			return (0);
		}
		*head = (*head)->next;
		cmp_tmp = cmp_tmp->next;
	}
	free_listint(cmp);
	return (1);
}
