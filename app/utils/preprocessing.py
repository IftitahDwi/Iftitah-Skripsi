import re
import string
import fasttext
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory,StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize

fasttext.FastText.eprint = lambda x: None

def case_folding(data_set=[]):
    result = list(map(lambda x: dict(x, **{"title": re.sub(r'[^\w\s]', '', re.sub(r"\d+", "", x["title"].lower()).strip())}), data_set))
    return result

def lang_detect(data_set=[]):
    DATA_TRAIN_LANGUAGE = "/home/hdinjos/Document/Iftitah-Skripsi/app/utils/model_language/lid.176.bin"
    model = fasttext.load_model(DATA_TRAIN_LANGUAGE)
    result = list(filter(lambda x: model.predict(x["title"])[0][0][9:] == "id", data_set))
    return result

def stopword(title_stop):
    stop_factory = StopWordRemoverFactory().get_stop_words()
    more_stopword = ['customer', 'relationship','fadegoretas','particle']
    data = stop_factory + more_stopword
    dictionary = ArrayDictionary(data)
    str = StopWordRemover(dictionary)
    stop = str.remove(title_stop)
    tokens = word_tokenize(stop)
    new_tokens = " ".join(tokens)
    return new_tokens

def stopword_title(data_set=[]):
    result = list(map(lambda x: dict(x, **{"title": stopword(x["title"])}), data_set))
    return result

def stemmed(data_set=[]):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    result = list(map(lambda x: dict(x, **{"title": stemmer.stem(x["title"])}), data_set))
    return result