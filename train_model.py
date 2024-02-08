import pandas as pd
from gensim.models.word2vec import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec

from globals import posts_file, vocab_file, output_file




def get_data():
    mapping = {"s":"rating_safe","q":"rating_questionable","e":"rating_explicit"}

    print("get_data: loading data")
    data = pd.read_csv(posts_file, engine="c") # Adjust chunksize as needed
    data = data.filter(items=["rating","tag_string"]).dropna()
    print("get_data: loading artist names")
    artist_names = pd.read_csv(vocab_file, engine="c").filter(items=["name","category"])
    artist_names = set(artist_names[artist_names['category'] == 1]['name']) # Use a set for faster lookup

    print("get_data: parsing data")
    data = (data['rating'].map(mapping)+ ' '+ data['tag_string']).str.split() # Use str.split() instead of transform

    print("get_data: converting artist tags")
    data = data.apply(lambda x: ["by_"+word if word in artist_names else word for word in x]) # Apply the function to each row
    return data.tolist()
class LossLogger(CallbackAny2Vec):
    '''Output loss at each epoch'''
    def __init__(self):
        self.epoch = 1
        self.losses = []

    def on_epoch_begin(self, model):
        print(f'Epoch: {self.epoch}', end='\t')

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        self.losses.append(loss)
        print(f'  Loss: {loss}')
        self.epoch += 1

def gen_model():
    print("getting data")
    data = get_data()
    print("building model")
    model = Word2Vec(data, min_count=10,workers=6,epochs=15)
    print("saving as wv")
    model.wv.save(output_file)

gen_model()