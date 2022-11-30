#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *tmp, *insert = malloc(sizeof(listint_t));

	if (insert == NULL)
		return (NULL);

	insert->n = number;

	curr = *head;

	if (*head == NULL)
	{
		curr = insert;
		curr->n = number;
		curr->next = NULL;
		*head = curr;
		return (*head);
	}

	while (curr->next != NULL)
	{
		if (curr->n > number)
		{
			*head = insert;
			insert->next = curr;
			return(*head);
		}
		if (curr->next->n >= number)
		{
			tmp = curr->next;
			curr->next = insert;
			insert->next = tmp;
			return(*head);
		}
		curr = curr->next;
	}

	curr->next = insert;
	insert->next = NULL;

	return (*head);
}
