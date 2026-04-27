from typing import Optional, Final
from dataclasses import dataclass

@dataclass
class Contact:
    """Enterprise entity representing a contact."""
    name: str
    phone_number: str
    email: str

class ContactNode:
    """Represent a node in the Singly Linked List."""
    def __init__(self, contact: Contact):
        self.contact: Contact = contact
        self.next: Optional['ContactNode'] = None

class ContactBook:
    """
    Production-grade Contact Management System using a Singly Linked List.
    
    Attributes:
        head (Optional[ContactNode]): The starting node of the contact list.
        _count (int): Internal tracker for the number of contacts.
    """

    def __init__(self):
        self._head: Optional[ContactNode] = None
        self._count: int = 0

    def insert_contact(self, name: str, phone: str, email: str) -> None:
        """
        Inserts a contact at the head of the list.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_contact = Contact(name, phone, email)
        new_node = ContactNode(new_contact)
        
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def find_contact(self, name: str) -> Optional[Contact]:
        """
        Searches for a contact by name.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        current = self._head
        while current:
            if current.contact.name.lower() == name.lower():
                return current.contact
            current = current.next
        return None

    def update_contact(self, name: str, new_phone: Optional[str] = None, new_email: Optional[str] = None) -> bool:
        """
        Updates an existing contact's details.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        current = self._head
        while current:
            if current.contact.name.lower() == name.lower():
                if new_phone:
                    current.contact.phone_number = new_phone
                if new_email:
                    current.contact.email = new_email
                return True
            current = current.next
        raise KeyError(f"Contact '{name}' not found.")

    def delete_contact(self, name: str) -> bool:
        """
        Removes a contact by name and repairs the chain.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not self._head:
            raise KeyError("Contact book is empty.")

        # Case 1: Head deletion
        if self._head.contact.name.lower() == name.lower():
            self._head = self._head.next
            self._count -= 1
            return True

        # Case 2: Middle or Tail deletion
        prev = self._head
        current = self._head.next
        
        while current:
            if current.contact.name.lower() == name.lower():
                prev.next = current.next
                self._count -= 1
                return True
            prev = current
            current = current.next

        raise KeyError(f"Contact '{name}' not found.")

    @property
    def total_contacts(self) -> int:
        return self._count
