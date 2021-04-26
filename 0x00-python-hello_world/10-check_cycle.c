#include "lists.h"

/**
 * check_cycle - Entry Point
 *
 * @list: type listint_t
 *
 * Description: check if list is cycle
 *
 * Return: 1 true, 0 false
 */

int check_cycle(listint_t *list)
{
	listint_t *node1 = list, *node2 = list;

	while (node1 != NULL && node2 != NULL && node2->next != NULL)
	{
		node1 = node1->next;
		node2 = node2->next->next;
		if (node1 == node2)
			return (1);
	}
	return (0);
}
