REM     --weights ./data/yolov3.weights ^
REM     --weights ./checkpoints/yolov3.ckpt ^

python ./tools/train.py ^
    --dataset ./data/voc2012_train_fire.tfrecord ^
    --val_dataset ./data/voc2012_val_fire.tfrecord ^
    --tiny False ^
    --weights --weights ./data/yolov3.weights ^
    --classes ./data/fire_voc2012.names ^
    --mode fit ^
    --transfer none ^
    --size 416 ^
    --epochs 100 ^
    --batch_size 2 ^
    --learning_rate 1e-5 ^
    --num_classes 1 ^
    --weights_num_classes 80
    