import os

# Get file list, and save list into txt
command='python '+'./data/get_file_list.py'+' '\
    '--classname runway'+' '\
    '--dataset_path ./data/VOC2012/'+' '\
    '--percent_train 0.9'
os.system(command)
command=''

command='python '+'./tools/voc2012.py'+' '\
    '-data_dir ./data/VOC2012/'+' '\
    '--split train'+' '\
    '--output_file ./data/voc2012_train_runway.tfrecord'+' '\
    '--classes ./data/runway.names'
os.system(command)
command=''

command='python '+'./tools/voc2012.py'+' '\
    '-data_dir ./data/VOC2012/'+' '\
    '--split val'+' '\
    '--output_file ./data/voc2012_val_runway.tfrecord'+' '\
    '--classes ./data/runway.names'
os.system(command)
command=''