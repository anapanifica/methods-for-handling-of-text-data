import stanza
nlp = stanza.Pipeline('abq',
                      dir="abq_stanza_resources",
                      processors='tokenize,lemma',
                      tokenize_model_path='stanza/saved_models/tokenize/abq_test_tokenizer.pt',
                      lemma_model_path='stanza/saved_models/lemma/abq_test_lemmatizer.pt',
                      download_method=None)
doc = nlp("сара сыхьиз фатимапI")
print(doc)
