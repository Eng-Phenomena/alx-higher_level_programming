#include "lists.h"

/**
 * check_cycle - checks if inked list is a ring or not
 * @list: the header of the list
 * Return: 1 if yes or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *start = list, *end = list;

	while (end)
	{
		end = end->next;
		if (end == start)
			return (1);
	}
	return (0);
}
