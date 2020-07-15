REM     --weights ./data/yolov3.weights ^
REM     --weights ./checkpoints/yolov3.ckpt ^

python ./tools/train.py ^
    --dataset ./data/voc2012_train_runway.tfrecord ^
    --val_dataset ./data/voc2012_val_runway.tfrecord ^
    --weights ./checkpoints/yolov3.tf ^
    --classes ./data/runway.names ^
    --mode fit ^
    --transfer darknet ^
    --size 416 ^
    --epochs 100 ^
    --batch_size 1 ^
    --learning_rate 1e-3 ^
    --num_classes 1 ^
    --weights_num_classes 80