import os

command = ''
command += 'python ' + './tools/detect.py' + ' '
command += '--classes' + ' ' + './data/classes/runway.names' + ' '
command += '--num_classes' + ' ' + '1' + ' '
command += '--tiny' + ' '
command += '--weights' + ' ' + './checkpoints/yolov3-tiny_train.ckpt' + ' '
command += '--image' + ' ' + './data/runway.S' + ' '
command += '--yolo_score_threshold' + ' ' + '0.01' + ' '

print(command)
os.system(command)
