import re
import colorsys
from gensim.models.keyedvectors import KeyedVectors
from globals import output_file
    


def read_kv():
    return KeyedVectors.load(output_file)
#gen_model()
#save_data_to_json()
def close_enough(KV: KeyedVectors, input):
    if input == "" or input == None: return None
    vocab = KV.index_to_key
    if input in vocab: return input
    for v in vocab:
        if input in v: 
            print("close enough: ", v)
            return v
    return None
def print_colored_titles(title_list):
    for i, (title, value) in enumerate(title_list):
        # Convert value to a hue in the range [0 (red), 1/3 (yellow), 2/3 (green)]
        hue = value/3.5
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        # Convert RGB to 8-bit per channel value (range 0-255)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        # Print the title with the color
        print(f'\033[38;2;{r};{g};{b}m{title}\033[0m', end='')
        if i != len(title_list) - 1:
            print(", ", end='')
    print("")
def runGUI():
    KV = read_kv() #type: KeyedVectors
    while(True):
        positive = input("positive: ")
        positive = [close_enough(KV, inp) for inp in re.sub("\s*,\s*",",",positive).replace(" ","_").split(",")]
        positive = list(filter(None, positive))
        negative = input("negative: ")
        negative = [close_enough(KV, inp) for inp in re.sub("\s*,\s*",",",negative).replace(" ","_").split(",")]
        negative = list(filter(None, negative))
        top = input("top: ")
        top = int(top or 10)
        try:
            similar = KV.most_similar(positive=positive, negative=negative, topn=top)
            print("related tags: ")
            print_colored_titles(similar)
            print("")

            
        
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
#gen_model()
runGUI()