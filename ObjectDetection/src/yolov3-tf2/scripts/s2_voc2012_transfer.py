import os

print('Read the file list and save to the txt')
'''
paremter list
'''
dataset_dir='./data/dataset/runway_VOC2012/'
class_path='./data/classes/runway.names'
class_name='runway'


# Get file list, and save list into txt
command=''
command+='python '+'./data/dataset/voc_convert2txt.py'+' '
command+='--classname'+' '+class_name+' '
command+='--dataset_path'+' '+dataset_dir+' '
command+='--percent_train 0.6'      # 训练集占数据集的比重
print(command)
os.system(command)


# transfer voc train dataset to tfrecords
command=''
command+='python '+'./tools/voc2012.py'+' '
command+='-data_dir'+' '+dataset_dir+' '
command+='--split train'+' '
command+='--output_file ./data/tfrecords/voc2012_train_'+class_name+'.tfrecord'+' '
command+='--classes'+' '+class_path
print(command)
os.system(command)

# transfer voc val dataset to tfrecords
command=''
command+='python '+'./tools/voc2012.py'+' '
command+='-data_dir'+' '+dataset_dir+' '
command+='--split val'+' '
command+='--output_file ./data/tfrecords/voc2012_val_'+class_name+'.tfrecord'+' '
command+='--classes'+' '+class_path
print(command)
os.system(command)
