#include "lists.h"
#include <stdlib.h>

/**
 * reverse_listint - Reverses a linked list
 * @head: pointer header
 * Return: reversed linked list.
 */
listint_t *reverse(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checking if linked listis a plaindrome
 * @head: head of list
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *rev, *mid;
	int size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse(&tmp);
	mid = rev;
	tmp = *head;

	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse(&mid);

	return (1);
}
