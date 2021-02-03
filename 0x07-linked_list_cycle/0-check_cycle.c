#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to check.
 * tagged as "tortoise and hare"
 * Return: returns 1 if there is a cycle otherwise 0
**/
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list;


	while ((tortoise) && (hare) && (list->next))
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
