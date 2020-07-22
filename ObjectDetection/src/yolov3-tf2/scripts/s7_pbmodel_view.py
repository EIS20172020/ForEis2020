import netron
import os

modelPath = "./model/yolov3-tiny_train/saved_model.pb"
# modelPath = os.getcwd()+"/checkpoints/yolov3-tiny_train.ckpt.index"
print(modelPath)
netron.start(modelPath,port=8081)