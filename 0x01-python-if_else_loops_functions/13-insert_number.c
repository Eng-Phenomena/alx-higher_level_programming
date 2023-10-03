#include "lists.h"

/**
 * insert_node - insering a new node to a linked list
 * @head: list head node
 * @number: num of node object
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (tmp && tmp->next && (tmp->next)->n < number)
		tmp = tmp->next;
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
