
import random

def main():
    for tense, quantity in [('past', 'single'), ('present', 'single'), ('future', 'single'),
                             ('past', 'plural'), ('present', 'plural'), ('future', 'plural')]:
        sentence = make_sentence(tense, quantity)
        print(sentence)

def make_sentence(tense, quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(tense, quantity)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = determiner + " " + noun + " " + verb + " " + prepositional_phrase + "."
    return sentence.capitalize()

def get_determiner(quantity):
    if quantity == 'single':
        determiners = ["a", "an", "the", "this", "that"]
    else:
        determiners = ["some", "many", "these", "those"]
    return random.choice(determiners)

def get_noun(quantity):
    nouns = ["dog", "cat", "bird", "child", "car", "rabbit", "girl", "boy"]
    noun = random.choice(nouns)
    return noun if quantity == 'single' else noun + "s"

def get_verb(tense, quantity):
    verbs = {
        'past': ["ran", "walked", "talked", "laughed", "drank"],
        'present': ["runs", "walks", "talks", "laughs", "drinks"],
        'future': ["will run", "will walk", "will talk", "will laugh", "will drink"]
    }
    verb = random.choice(verbs[tense])
    return verb if quantity == 'single' else verb.replace("s", "") if tense == 'present' else verb

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + " " + determiner + " " + noun
    return prepositional_phrase

if __name__ == "__main__":
    main()

