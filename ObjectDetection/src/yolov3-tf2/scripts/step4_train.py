import os

print('Train')
'''
parameter list
'''
dataset_dir = './data/dataset/runway_VOC2012/'
class_path = './data/classes/runway.names'
class_name = 'runway'

command = ''
command += 'python ' + './tools/train.py' + ' '
command += '--dataset ./data/tfrecords/voc2012_train_' + class_name + '.tfrecord' + ' '
command += '--val_dataset ./data/tfrecords/voc2012_val_' + class_name + '.tfrecord' + ' '
command += '--weights ./checkpoints/yolov3.tf' + ' '
command += '--classes ./data/classes/' + class_name + '.names' + ' '
command += '--mode fit' + ' '
command += '--transfer darknet' + ' '
command += '--size 416' + ' '
command += '--epochs 100' + ' '
command += '--batch_size 1' + ' '
command += '--learning_rate 1e-3' + ' '
command += '--num_classes 1' + ' '
command += '--weights_num_classes 80'
print(command)
os.system(command)
