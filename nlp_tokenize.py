from nltk import (
    PorterStemmer, LancasterStemmer,
    word_tokenize, wordpunct_tokenize, sent_tokenize
)
import yaml
porter = PorterStemmer()
lancaster = LancasterStemmer()

line = "\n"+"="*80+"\n"

def stem_passage(passage,punct_tokenize = False):
    return " ".join(
        stem_sentence(sentence,punct_tokenize)
        for sentence in sent_tokenize(passage)
    )

def stem_sentence(sentence,punct_tokenize=False):
    tokenizer_func = wordpunct_tokenize if punct_tokenize else word_tokenize
    return " ".join(
        porter.stem(word)
        for word in tokenizer_func(sentence)
    )

if __name__ == "__main__":
    with open("stemming.yaml") as f:
        stemming_words, stemming_passage = yaml.full_load(f).values()
    print(
        "STEMMING WORDS:\n",
        "STEMMER COMPARISION:\n",sep = "\n"
    )
    print("-"*64)
    print(f"|{'WORD':^20}|{'PORTER STEMMER':^20}|{'LANCASTER STEMMER':^20}|")
    print("-"*64)
    for word in stemming_words:
        print(f"|{word:^20}|{porter.stem(word):^20}|{lancaster.stem(word):^20}|")
    print("-"*64)
    print(line)

    print("STEMMING PASSAGES:\n")
    
    print(
        "ORIGINAL PASSAGE :\n",
        stemming_passage,
        "\nSTEMMED PASSAGE :\n",
        stem_passage(stemming_passage),
        "\nSTEMMED PASSAGE (using wordpunct_tokenizer) :\n",
        stem_passage(stemming_passage,True),sep="\n"
    )
    print(line)