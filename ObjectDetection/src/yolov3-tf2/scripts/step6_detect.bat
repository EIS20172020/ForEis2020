
python ./tools/detect.py ^
	--classes ./data/fire_voc2012.names ^
	--num_classes 1 ^
	--weights ./checkpoints/yolov3_train.tf ^
	--image ./data/fire.jpg ^
    --yolo_score_threshold 0.1