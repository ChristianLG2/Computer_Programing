
from TroubleShooting import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase

def test_get_determiner():
    determiner = get_determiner()
    assert determiner in ["a", "an", "the", "this", "that"]

def test_get_noun():
    noun = get_noun()
    assert noun in ["dog", "cat", "bird", "child", "car", "rabbit", "girl", "boy"]

def test_get_verb():
    verb = get_verb()
    assert verb in ["runs", "walks", "talks", "laughs", "drinks"]

def test_get_preposition():
    preposition = get_preposition()
    assert preposition in ["above", "in", "on", "over", "before", "about", "for", "with", "to", "from"]

def test_get_prepositional_phrase():
    prepositional_phrase = get_prepositional_phrase()
    assert isinstance(prepositional_phrase, str)
