REM Train
python ./tools/voc2012.py ^
    --data_dir ./data/voc2012_raw/VOCdevkit/VOC2012/ ^
    --split train ^
    --output_file ./data/voc2012_train_fire.tfrecord ^
    --classes ./data/fire_voc2012.names

REM Val
python tools/voc2012.py ^
    --data_dir ./data/voc2012_raw/VOCdevkit/VOC2012/ ^
    --split  val ^
    --output_file ./data/voc2012_val_fire.tfrecord ^
    --classes ./data/fire_voc2012.names