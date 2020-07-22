import os

abspath=os.path.abspath('.')
print(abspath)

command = ''
command += 'python ' + 'D:/Programs/IntelSWTools/openvino_2020.4.287/deployment_tools/model_optimizer/mo_tf.py' + ' '
command += '--input_model' + ' ' + abspath+'/model/yolov3-tiny_train/saved_model.pb' + ' '
command += '--input_checkpoint' + ' ' + abspath+'/checkpoints' + ' '
command += '--input_shape' + ' ' + '[1,416,416,3]' + ' '
command += '--output' + ' ' + abspath+'/model/' + ' '
command += '--mean_values' + ' ' + '[127.5,127.5,127.5]' + ' '
command += '--scale_values' + ' ' + '[127.5,127.5,127.5]' + ' '

# command += '--weights_num_classes 80'

print(command)
os.system(command)
