# Phone Directory (Hash Map)

### Architectural Overview
The **Phone Directory** is implemented using a **Hash Map** to provide $O(1)$ average-time complexity for contact management.

**Core Design Decisions:**
1.  **Key-Based Retrieval:** Uses the contact's name as a unique hash key, ensuring instant lookups regardless of directory size.
2.  **Case-Insensitive Normalization:** Normalizes all keys to lowercase and trims whitespace to prevent duplicate entries from formatting inconsistencies.
3.  **Atomic CRUD Operations:** Encapsulates Create, Read, Update, and Delete logic with strict validation to maintain data integrity.
4.  **Exception Safety:** Implements defensive checks that raise standardized Python exceptions (`ValueError`, `KeyError`) for invalid operations.

### Complexity Analysis
- **Add Contact:** Average $O(1)$
- **Search (by Name):** Average $O(1)$
- **Update Contact:** Average $O(1)$
- **Delete Contact:** Average $O(1)$
- **Space:** $O(N)$
