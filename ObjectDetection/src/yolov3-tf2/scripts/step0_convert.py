import os

# Conert yolov3 official darknet weight into tensorflow .tf
command='python'+' '+'../tools/convert.py'+' '\
    '--output ./checkpoints/yolov3.tf'+' '\
    '--num_classes 80'
os.system(command)
command=''

# Conert yolov3 official darknet weight into tensorflow .ckpt
command='python'+' '+'../tools/convert.py'+' '\
    '--output ./checkpoints/yolov3.ckpt'+' '\
    '--num_classes 80'
os.system(command)
command=''
