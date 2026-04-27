import pytest
from chatbot_suggestion_engine import ChatbotEngine

def test_chatbot_suggestions():
    engine = ChatbotEngine()
    engine.add_intent("help", "HELP_INTENT", "How can I assist you?")
    engine.add_intent("help login", "LOGIN_ISSUE", "Please reset your password.")
    
    assert engine.get_suggestion("help") == "How can I assist you?"
    assert engine.get_suggestion("help login quickly") == "Please reset your password."
    assert engine.get_suggestion("hello") is None
