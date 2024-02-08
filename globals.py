import os

working_dir = os.getcwd()
dataset_dir = os.path.join(working_dir, "datasets")
posts_file = os.path.join(dataset_dir, "posts.csv")
vocab_file = os.path.join(dataset_dir, "tags.csv")
output_file = os.path.join(working_dir, "out.kv")
