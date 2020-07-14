import os
import glob

from absl import app
from absl import flags
import os
 
FLAGS = flags.FLAGS
 
flags.DEFINE_string('classname', 'runway', '.')
flags.DEFINE_string('dataset_path','./data/VOC2012/','.')
flags.DEFINE_float('percent_train' , 0.9,'.')


def main(argv):
    """
    Parameter needed to change
    """
    classname=FLAGS.classname
    dataset_path = FLAGS.dataset_path
    percent_train = FLAGS.percent_train

    # -------- Run --------
    img_path = dataset_path+'JPEGImages'
    try:
        path_list = os.listdir(img_path)
    except OSError:
        print('[Error]', 'don\'t exsit the path', img_path)
    path_list.sort()
    len_dataset = len(path_list)
    print('[Info]', "Find", len_dataset, "images in dataset")

    file_list_path = dataset_path+'ImageSets/Main'+'/'
    train_txt_path = file_list_path+classname+'_train.txt'
    val_txt_path = file_list_path+classname+'_val.txt'

    len_train=int(len_dataset*percent_train)

    with open(train_txt_path, 'wt') as f:
        for img_filename in path_list[0:len_train]:
            content = img_filename[:-4]+" -1"
            f.write(content)
            if img_filename!=path_list[len_train-1]:
                f.write('\n')

    with open(val_txt_path, 'wt') as f:
        for img_filename in path_list[len_train:-1]:
            content = img_filename[:-4]+" -1"
            f.write(content)
            if img_filename!=path_list[-2]:
                f.write('\n')
    


if __name__ == "__main__":
    app.run(main)
