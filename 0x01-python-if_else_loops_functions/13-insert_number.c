#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *tmp, *insert = malloc(sizeof(listint_t));

	if (insert == NULL)
		return (NULL);

	insert->n = number;

	curr = *head;

	if (curr == NULL)
	{
		curr->n = number;
		return (*head);
	}

	while (curr->next != NULL)
	{
		if (curr->next->n >= number)
		{
			tmp = curr->next;
			curr->next = insert;
			insert->next = tmp;
			break;
		}
		curr = curr->next;
	}
	return (*head);
}
