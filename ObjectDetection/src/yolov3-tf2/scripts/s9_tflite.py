import os

print('command')

command = ''
command += 'python' + ' '+'D:/Programs/IntelSWTools/openvino_2020.4.287/deployment_tools/model_optimizer/mo_tf.py'
command += '--saved_model_dir' + '=' + './model/yolov3-tiny_train' + ' '
command += '--output_file' + '=' + './tflite/model.tflite' + ' '


print(command)
os.system(command)
