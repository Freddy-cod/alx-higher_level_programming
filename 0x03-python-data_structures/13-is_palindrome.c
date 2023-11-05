#include "lists.h"

/**
 * is_palindrome - function that checks palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - check if list is palindrome
 * @head: pointer to the head of the list
 * @last: pointer to the tail of the list
 * Return: 0 if not palindrom else 1
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
