from spellchecker import SpellChecker
from nltk import word_tokenize
import yaml
spell = SpellChecker()

line = "\n"+"="*80+"\n"
    
if __name__ == "__main__":
    with open("spell_checking.yaml") as f:
        sentence,spell_check_words = yaml.full_load(f).values()
    words = word_tokenize(sentence)
    misspelled_words = spell.unknown(words)
    correct_sentence = " ".join(spell.correction(word) for word in words)
    print(
        "SPELL CORRECTION:",
        "\nORIGINAL SENTENCE:\n",
        sentence,
        "\nWORDS:\n",
        ", ".join(words),
        "\nMISSPELLED WORDS:\n",
        ", ".join(misspelled_words),
        "\nCORRECTED SENTENCE:\n",
        correct_sentence,sep="\n"
    )
    print(line)
    print("SPELL CHECKER TESTS:")
    
    print("-"*80)
    print(f"|{'WORD':^13}|{'PROBABILITY':^15}|{'CANDIDATES':^32}|{'CORRECTION':^15}|")
    print("-"*80)
    for word in spell_check_words:
        print(
            f"|{word:^13}"
            f"|{spell.word_usage_frequency(word):^15.3}"
            f"|{', '.join(spell.candidates(word)):^32}"
            f"|{spell.correction(word):^15}|"
        )
    print("-"*80)
    print(line)