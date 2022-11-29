#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: The list to check.
 *
 * Return: 0 If there is no cycle
 * 1 If there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *speed;

	if (list == NULL || list->next == NULL)
		return (0);

	snail = list->next;
	speed = list->next->next;

	while (snail && speed && speed->next)
	{
		if (snail == speed)
			return (1);

		snail = snail->next;
		speed = speed->next->next;
	}

	return (0);
}
