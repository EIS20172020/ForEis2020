import os

# Conert yolov3 official darknet weight into tensorflow .tf
command = ''
command += 'python' + ' ' + './tools/convert.py' + ' '
command += '--weights ./data/pre-weights/yolov3.weights' + ' '
command += '--output ./checkpoints/yolov3.tf' + ' '
command += '--num_classes 80'
os.system(command)
command = ''

# Conert yolov3 official darknet weight into tensorflow .ckpt
command = ''
command += 'python' + ' ' + './tools/convert.py' + ' '
command += '--weights ./data/pre-weights/yolov3.weights' + ' '
command += '--output ./checkpoints/yolov3.ckpt' + ' '
command += '--num_classes 80'

os.system(command)
command = ''
