import nltk
# import pdb

nltk.data.path.append("/Users/jianqiaoliu/Downloads/nltk_data")

sample = 'I study computer science at Purdue University. The president is Mitch Daniels. Indiana State is the Hoosier State.'

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'PERSON' or t.label() == 'ORGANIZATION' or t.label() == 'LOCATION':
            # pdb.set_trace()
            entity_names.append([' '.join([child[0] for child in t]), t.label()])
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print(entity_names)