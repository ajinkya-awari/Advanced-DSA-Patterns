from typing import Dict, Optional, Final
from dataclasses import dataclass

@dataclass
class Contact:
    """Represents a contact entity in the directory."""
    name: str
    phone_number: str

class PhoneDirectory:
    """
    Enterprise-grade Phone Directory using Hash Map for O(1) retrieval.
    
    Attributes:
        _directory (Dict[str, Contact]): Internal hash-based storage.
    """

    def __init__(self):
        self._directory: Dict[str, Contact] = {}

    def _normalize_key(self, name: str) -> str:
        """Normalizes the name key for case-insensitive lookup."""
        return name.strip().lower()

    def add_contact(self, name: str, phone_number: str) -> None:
        """
        Adds a new contact to the directory.
        
        Time Complexity: O(1) average.
        Space Complexity: O(1) for the new entry.
        """
        if not name or not name.strip():
            raise ValueError("Contact name cannot be empty.")
        
        normalized_name = self._normalize_key(name)
        if normalized_name in self._directory:
            raise ValueError(f"Contact '{name}' already exists.")

        self._directory[normalized_name] = Contact(name.strip(), phone_number.strip())

    def get_contact(self, name: str) -> Contact:
        """
        Retrieves contact details by name.
        
        Time Complexity: O(1) average.
        """
        normalized_name = self._normalize_key(name)
        if normalized_name not in self._directory:
            raise KeyError(f"Contact '{name}' not found.")
        return self._directory[normalized_name]

    def update_contact(self, name: str, new_phone: str) -> None:
        """
        Updates the phone number for an existing contact.
        
        Time Complexity: O(1) average.
        """
        normalized_name = self._normalize_key(name)
        if normalized_name not in self._directory:
            raise KeyError(f"Contact '{name}' not found.")
        
        self._directory[normalized_name].phone_number = new_phone.strip()

    def delete_contact(self, name: str) -> None:
        """
        Removes a contact from the directory.
        
        Time Complexity: O(1) average.
        """
        normalized_name = self._normalize_key(name)
        if normalized_name not in self._directory:
            raise KeyError(f"Contact '{name}' not found.")
        
        del self._directory[normalized_name]

    @property
    def total_contacts(self) -> int:
        return len(self._directory)
