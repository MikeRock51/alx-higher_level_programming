#include "lists.h"

/*
 * insert_node - Inserts a number in a sorted linked list
 * @head: Pointer to the first element on the list
 * @number: Number to be inserted in the list
 *
 * Return: A pointer to the first item on the list.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *tmp, *insert = malloc(sizeof(listint_t));

	if (insert == NULL)
		return (NULL);

	insert->n = number;

	curr = *head;


	if (curr->next == NULL)
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
