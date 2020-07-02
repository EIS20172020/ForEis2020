python train.py ^
	--dataset ./data/voc2012_train.tfrecord ^
	--val_dataset ./data/voc2012_val.tfrecord ^
	--classes ./data/voc2012.names ^
	--num_classes 20 ^
	--mode fit --transfer darknet ^
	--batch_size 16 ^
	--epochs 10 ^
	--weights ./checkpoints/yolov3.tf ^
	--weights_num_classes 80 