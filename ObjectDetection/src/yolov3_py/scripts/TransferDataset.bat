
python tools/voc2012.py ^
  --data_dir './data/voc2012_raw/VOCdevkit/VOC2012' ^
  --split train ^
  --output_file ./data/voc2012_train.tfrecord

python tools/voc2012.py ^
  --data_dir './data/voc2012_raw/VOCdevkit/VOC2012' ^
  --split val ^
  --output_file ./data/voc2012_val.tfrecord
