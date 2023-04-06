
import random

def main():
    sentence_count = 5
    for i in range(sentence_count):
        sentence = generate_sentence()
        print(sentence)

def generate_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    sentence = determiner + " " + noun + " " + verb + " " + prepositional_phrase + "."
    return sentence.capitalize()

def get_determiner():
    determiners = ["a", "an", "the", "this", "that"]
    return random.choice(determiners)

def get_noun():
    nouns = ["dog", "cat", "bird", "child", "car", "rabbit", "girl", "boy"]
    return random.choice(nouns)

def get_verb():
    verbs = ["runs", "walks", "talks", "laughs", "drinks"]
    return random.choice(verbs)

def get_preposition():
    prepositions = ["above", "in", "on", "over", "before", "about", "for", "with", "to", "from"]
    return random.choice(prepositions)

def get_prepositional_phrase():
    determiner = get_determiner()
    noun = get_noun()
    preposition = get_preposition()
    prepositional_phrase = preposition + " " + determiner + " " + noun
    return prepositional_phrase

if __name__ == "__main__":
    main()
