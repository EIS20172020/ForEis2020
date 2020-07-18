
python ./tools/detect.py ^
	--classes ./data/classes/runway.names ^
	--num_classes 1 ^
	--weights ./checkpoints/yolov3_train.tf ^
	--image ./data/runway.jpg ^
    --yolo_score_threshold 0.1