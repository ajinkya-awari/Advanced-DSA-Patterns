from typing import Dict, List, Optional

class ChatbotNode:
    def __init__(self):
        self.children: Dict[str, 'ChatbotNode'] = {}
        self.intent_id: Optional[str] = None

class ChatbotEngine:
    """
    Maps intent prefixes to responses using Trie + HashMap.
    """

    def __init__(self):
        self._root = ChatbotNode()
        self._responses: Dict[str, str] = {}

    def add_intent(self, prefix: str, intent_id: str, response: str) -> None:
        current = self._root
        for char in prefix.lower():
            if char not in current.children:
                current.children[char] = ChatbotNode()
            current = current.children[char]
        current.intent_id = intent_id
        self._responses[intent_id] = response

    def get_suggestion(self, user_input: str) -> Optional[str]:
        """Finds the most specific intent matching the user input."""
        current = self._root
        last_intent = None
        for char in user_input.lower():
            if char not in current.children:
                break
            current = current.children[char]
            if current.intent_id:
                last_intent = current.intent_id
        
        return self._responses.get(last_intent) if last_intent else None
