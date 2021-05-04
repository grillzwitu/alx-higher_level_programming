#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Entry Point.
 *
 * @head: Pointer to the head pointer of the Linked list.
 *
 * Description: Reverses a Linked list
 *
 * Return: The reverse of the linked list or Null
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *currentNode = *head;
	listint_t *nextNode;
	listint_t *prevNode = NULL;

	if (*head == NULL)
		return (NULL);
	while (currentNode)
	{
		nextNode = (*currentNode).next;
		(*currentNode).next = prevNode;
		prevNode = currentNode;
		currentNode = nextNode;
	}
	*head = prevNode;
	return (*head);
}

/**
 * is_palindrome - Entry Point.
 *
 * @head: Pointer to the head of the Linked list
 *
 * Description: Checks if a linked list is a palindrome
 *
 * Return: 0 if not a palindrome or 1 if success.
 */

int is_palindrome(listint_t **head)
{
	listint_t *auxList, *tmpList, *revList;
	int len, c;

	if (head == NULL || *head == NULL || (*(*head)).next == NULL)
		return (1);

	auxList = *head;
	for (len = 0; auxList; len++)
		auxList = (*auxList).next;

	tmpList = *head;
	for (c = 0; c < (len / 2) - 1; c++)
		tmpList = (*tmpList).next;

	if (len % 2 == 0 && (*tmpList).n != (*(*tmpList).next).n)
		return (0);

	tmpList = (*(*tmpList).next).next;
	revList = reverse_listint(&tmpList);
	auxList = revList;

	tmpList = *head;
	while (revList)
	{
		if ((*tmpList).n != (*revList).n)
			return (0);
		tmpList = (*tmpList).next;
		revList = (*revList).next;
	}
	reverse_listint(&auxList);

	return (1);
}
