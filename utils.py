# # ================================================= Startup codes for new notebooks
# %config Completer.use_jedi = False
# %load_ext autotime
# import sys
# from importlib import reload
# %load_ext autoreload
# %autoreload 2

# sys.path.append(r'C:\Alamin\Dropbox\Codes')
# sys.path.append(r'/home/mdabdullahal.alamin/alamin/Utility/')
# import Utility.utils as util
# from Utility.basic_modules import *

import glob, os, sys
import numpy as np
import pandas as pd
import csv
import pickle
import math
import pathlib
import shutil

def import_basic_modules():
    import tensorflow as tf

    print("Basic modules have been imported successfully")

def test():
    print("Util method test has been loaded correctly 6")


class Pandas:
    def __init__(self, base_dir):
        self.BASE_DIR = base_dir

    def save_df(self, df, file_name, append=False):
        dir_path = os.path.join(self.BASE_DIR, "output")
        Directory.create_directory(dir_path)
        file_name = os.path.join(dir_path, file_name)
        Pandas.static_save_df(df, file_name, append)


    def static_save_df(df, file_name, append=False):
        if append:
            df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, mode="a", header=False)
        else:
            df.to_csv(file_name, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        print("Dataframe has been saved in: %s" % (file_name))

    def load_obj(self, name):
        file_path = os.path.join(self.BASE_DIR, "pickle", name + ".pkl")
        return Pandas.static_load_obj(file_path)


    def static_load_obj(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def save_obj(self, obj, name):
        print("Base method")
        dir_path = os.path.join(self.BASE_DIR, "pickle")
        Directory.create_directory(dir_path)
        file_path = os.path.join(dir_path, name + ".pkl")
        Pandas.static_save_obj(obj, file_path)
        # with open(file_path, 'wb') as f:
        #     pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        # print("Saved object to a file: %s" % (str(file_path)))

    def static_save_obj(obj, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        print("Saved object to a file: %s" % (str(file_path)))

    def test(self):
        print("Pandas test")
        print(self.BASE_DIR)
        SO.test()




class Test:
    def __init__(self):
        pass
        




class Directory:
    def __init__(self):
        pass

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

    def remove_and_create_directory(dir):
        print("Going to REMOVE and CREATE directory: %s" % dir)
        Directory.remove_directory(dir)
        Directory.create_directory(dir)

    def get_list_of_image_from_directory(dir):
        res = list(pathlib.Path(dir).glob("**/*.jpg"))
        res += list(pathlib.Path(dir).glob("**/*.png"))
        print("Total %d images found in directory %s" % (len(res), dir))
        return res






class TF:
    def __init__(self):
        import tensorflow as tf
        print(tf.__version__)
        self.tf = tf

    def check_gpu(self):
        print("#" * 10)
        print("Num GPUs Available: ", len(self.tf.config.list_physical_devices('GPU')))
        print(self.tf.config.list_physical_devices('GPU'))


class Plot:
    def __init__(self):
        import matplotlib.pylab as plt
        import matplotlib.image as mpimg
        self.plt = plt
        self.mpimg = mpimg

    def image_visualization(self, image_paths, ncols=4, title=None):
        nrows = int(math.ceil(len(image_paths) * 1.0 / ncols))

        fig = self.plt.gcf()
        fig.set_size_inches(ncols*4, nrows*4)
        fig.tight_layout()
        if title is not None:
            fig.suptitle(title, fontsize="x-large")

        for i, img in enumerate(image_paths):
            img = self.mpimg.imread(img)
            sp = self.plt.subplot(nrows, ncols, i + 1)
            sp.axis('Off')
            self.plt.imshow(img)
        self.plt.show()
        self.plt.close()
        self.plt.cla()
        self.plt.clf()


import re
class SO:
    def __init__(self, dataset_dir):
        import lxml.etree  as ET
        self.ET = ET
        self.dataset_dir = dataset_dir
        self.Posts_COLS = ["Id", "PostTypeId", "AcceptedAnswerId", "ParentId", "CreationDate", "DeletionDate", "Score", "ViewCount", "Body",
        "OwnerUserId", "OwnerDisplayName", "LastEditorUserId", "LastEditorDisplayName", "LastEditDate", "LastActivityDate",
        "Title", "Tags", "AnswerCount", "CommentCount", "FavoriteCount", "ClosedDate", "CommunityOwnedDate", "ContentLicense"]
        self.POSTS_file = os.path.join(self.dataset_dir, "Posts.xml")
        

    def get_tags(tags_str):
        return re.findall(r'<(.+?)>', tags_str)

    def make_link(id, type):
        '''
        id = postid
        type : 'q' for question
                'a' for answer
        '''
        url = f'https://stackoverflow.com/{type}/{id}'
        return f'=HYPERLINK("{url}", "{id}")'

    def linkToId(link):
        '''
        Takes a excel styled link and retures the QuestionID
        '''
        return int(link.split('"')[::-1][1])
    
    def test():
        print("SO tests")


    
    def get_questions_from_tags(self, TAGS):
        Progress_Interval = 10000000

        # POSTS_file = os.path.join(self.dataset_dir, "Posts.xml")
        print("Going to extract questions from: %s \n and for the following tags: %s" % (POSTS_file, TAGS))

        context = self.ET.iterparse(self.POSTS_file, events=("end",))
        
        df_posts = pd.DataFrame(columns = self.Posts_COLS)
        total_questions = 0

        _, root = next(context)
        for event, elem in context:
            if elem.tag == "row":
                tags = elem.attrib.get('Tags', '')
                tags_list = SO.get_tags(tags) # list of tags
                for tag in TAGS:
                    if tag in tags_list:
                        dic = {}
                        for col in self.Posts_COLS:
                            dic[col] = elem.attrib.get(col, '')
                            # data.append(elem.attrib.get(col, ''))
                        df_posts = df_posts.append(pd.Series(dic), ignore_index = True)    
                        continue
                # progress
                if total_questions % Progress_Interval == 0:
                    print('done', elem.attrib['Id'])
                elem.clear()
                root.clear()
                total_questions += 1
        df_posts.drop_duplicates('Id', inplace=True)
        return df_posts

    def get_answers_from_questions(self, question_ids):
        question_ids = set(question_ids)

        context = self.ET.iterparse(self.POSTS_file, events=("end",))
        print("Going to extract answers")
        df_answers = pd.DataFrame(columns = self.Posts_COLS)
        total_answers = 0
        count = 0
        _, root = next(context)
        for event, elem in context:
            if elem.tag == "row":
                post_type = int(elem.attrib.get('PostTypeId'))
                if(post_type == 2):
                    parent_id = elem.attrib.get('ParentId')
                    if(parent_id in question_ids):
                        dic = {}
                        for col in self.Posts_COLS:
                            dic[col] = elem.attrib.get(col, '')
                        df_answers = df_answers.append(pd.Series(dic), ignore_index = True)    
                # progress
                if (int(elem.attrib['Id']) % 1000000) == 0:
                    print('done id: %s and len of res: %d' % (elem.attrib['Id'], len(df_answers)))
                total_answers += 1
                elem.clear()
                root.clear()
        print("Before removing duplicates Total answers: %d" % (len(df_answers)))
        df_answers.drop_duplicates('Id', inplace=True)        
        print("After removing duplicates Total answers: %d" % (len(df_answers)))
        return df_answers

    def generate_stats_POSTS(self):
        context = self.ET.iterparse(self.POSTS_file, events=("end",))
        print("Going to extract questions")
        total_posts = 0
        total_Q = 0
        total_A = 0
        total_Q_with_acc = 0
        all_post_ids = set()

        _, root = next(context)
        for event, elem in context:
            if elem.tag == "row":
                id = int(elem.attrib.get('Id'))
                if id in all_post_ids:
                    continue
                all_post_ids.add(id)
                total_posts += 1
                post_type = int(elem.attrib.get('PostTypeId'))            
                if(post_type == 1):
                    total_Q += 1
                    acc_id = (elem.attrib.get('AcceptedAnswerId'))
                    if(acc_id is not None and len(acc_id) > 4):
                        total_Q_with_acc += 1                    
                else:
                    total_A += 1
                # progress
                if total_posts % 10000000 == 0:
                    print('done', elem.attrib['Id'])
                    # break
                elem.clear()
                root.clear()
        print("total_posts: %d, total_Q: %d, total_A: %d, total_Q_with_acc: %d" % (total_posts, total_Q, total_A, total_Q_with_acc))
        return total_posts, total_Q, total_A, total_Q_with_acc

    # total_posts, total_Q, total_A, total_Q_with_acc = selfgenerate_final_stats(POSTS_file)
    # print(total_posts, total_Q, total_A, total_Q_with_acc)
    # print("total_posts: %d, total_Q: %d, total_A: %d, total_Q_with_acc: %d" % (total_posts, total_Q, total_A, total_Q_with_acc))