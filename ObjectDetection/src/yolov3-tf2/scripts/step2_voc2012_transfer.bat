@echo Read the file list and save to the .txt
python ./scripts/get_file_list.py ^
    --classname runway ^
    --dataset_path ./data/VOC2012/ ^
    --percent_train 0.9

@echo conver Train dataset to tfrecord
python ./tools/voc2012.py ^
    --data_dir ./data/VOC2012/ ^
    --split train ^
    --output_file ./data/voc2012_train_runway.tfrecord ^
    --classes ./data/runway.names

@echo conver Val dataset to tfrecord
python tools/voc2012.py ^
    --data_dir ./data/VOC2012/ ^
    --split  val ^
    --output_file ./data/voc2012_val_runway.tfrecord ^
    --classes ./data/runway.names

