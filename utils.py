import glob, os, sys
import matplotlib.pylab as plt
import numpy as np
# import tensorflow as tf
# print(tf.__version__)
import pandas as pd
import csv
import pickle
import math
import pathlib
import shutil
import tensorflow as tf
import matplotlib.image as mpimg


def save_df(df, file_name, append=False):
    if append:
        df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, mode="a", header=False)
    else:
        df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)


def load_obj(base_dir, name):
    file_path = os.path.join(base_dir, "pickle", name + ".pkl")
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def save_obj(obj, base_dir, name):
    dir_path = os.path.join(base_dir, "pickle")
    create_directory(dir_path)
    file_path = os.path.join(dir_path, name + ".pkl")
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    print("Saved object to a file: %s" % (str(file_path)))


def save_df(df, base_dir, file_name):
    file_name = os.path.join(base_dir, file_name)
    df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

def remove_directory(path):
    if os.path.exists(path):
        print("%s path exists and removing it." % path)
        shutil.rmtree(path)

def remove_file(file_name):
    if (os.path.isfile(file_name)):
        print("Output file %s exists and removing it." % file_name)
        os.remove(file_name)

def create_directory(dir):
    if(not os.path.exists(dir)):
        print("Creating directory %s." % dir)
        os.makedirs(dir)
    else:
        print("Directory %s already exists and so returning." % dir)

def test():
    print("Util method test has been loaded correctly")

def test2():
    print("Util method test 2 has been loaded correctly")


def remove_and_create_directory(dir):
    print("Going to REMOVE and CREATE directory: %s" % dir)
    remove_directory(dir)
    create_directory(dir)

def get_list_of_image_from_directory(dir):

    res = list(pathlib.Path(dir).glob("**/*.jpg"))
    res += list(pathlib.Path(dir).glob("**/*.png"))
    print("Total %d images found in directory %s" % (len(res), dir))
    return res

# get_list_of_image_from_directory(dataset_simulated_dir)


def check_gpu():
    print("#" * 10)
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print(tf.config.list_physical_devices('GPU'))



def image_visualization(image_paths, ncols=4, title=None):
    nrows = int(math.ceil(len(image_paths) * 1.0 / ncols))

    fig = plt.gcf()
    fig.set_size_inches(ncols*4, nrows*4)
    fig.tight_layout()
    if title is not None:
        fig.suptitle(title, fontsize="x-large")

    for i, img in enumerate(image_paths):
        img = mpimg.imread(img)
        sp = plt.subplot(nrows, ncols, i + 1)
        sp.axis('Off')
        plt.imshow(img)
    plt.show()
    plt.close()
    plt.cla()
    plt.clf()