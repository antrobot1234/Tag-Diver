# Tag Diver

this is a basic python project I set up to train a word2vec model on tags and use it to inspect the relationships betweent ags

## usage

To use the program, first, run `setup.bat`. it will set up the python env for the project.
then, run `launch.bat`. you should then be able to input positve and negative tags you want to find similar tags for.
to search for multiple prompts, separate your tags with commas.

## folders
all the directories that this project expects are stored in `globals.py`. if you want to change where it outputs and reads files from, change them there.
## training
if you want to train the model yourself, there are a couple of steps you are going to need to do
1. download the csv image and tag lists.
2. put them in the datasets directory. the default file names it expects are `posts.csv` and `tags.csv` respectively
3. run the `train_model.py` file. it should then output a trained model into the file specified by `globals.py`