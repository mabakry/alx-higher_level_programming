#include "lists.h"
#include <stdlib.h>

/**
 * reverse_listint - reverse a list
 * @head: list
 * Return: address of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
        listint_t *prev = NULL, *next = NULL, *current = *head;

        while (current)
        {
                next = current->next;
                current->next = prev;
                prev = current;
                current = next;
        }
        current = prev;
        return (current);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list to be checked.
 * Return: 0 if not palindrome, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *cmp = NULL;

	if (*head == NULL || temp->next == NULL)
		return (1);

	cmp = reverse_listint(head);
	while (temp && cmp && temp->next && cmp->next)
	{
		if (temp->n != cmp->n)
			return (0);
		
		temp = temp->next;
		cmp = cmp->next;
	}
	return (1);
}
