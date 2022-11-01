from gensim.models import word2vec
model = word2vec.Word2Vec.load("./wiki.model")
results = model.wv.most_similar(positive=['word', 'word'], negative=['word', 'word'], topn=20)
for result in results:
    print(result)
