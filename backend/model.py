
from transformers import pipeline,TFBertForTokenClassification

class LanguageModel:
    def __init__(self, nlp):
        self.nlp = nlp

    def named_entity_recognition(self, text):
        l = []
        t = self.nlp(text)
        in_word=False

        for i,token in enumerate(t):
            if token['entity'] == 'O':
                in_word = False
                continue

            if token['word'].startswith('##'):
                # deal with (one level of) orphaned ##-tokens
                if not in_word:
                    l += [ t[i-1] ]
                    l[-1]['entity'] = token['entity']
                
                l[-1]['word'] += token['word'][2:]
            else:
                l += [ token ]

            in_word = True

        #print(l)
        return(l)


