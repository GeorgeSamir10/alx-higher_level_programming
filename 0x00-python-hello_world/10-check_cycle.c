#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	int cycle_flag = 0;

	if (list == NULL)
		return (0);
	slow = fast = list;
	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = (fast->next)->next;
		if (fast == slow)
			return (1);
	}
	return (cycle_flag);
}
