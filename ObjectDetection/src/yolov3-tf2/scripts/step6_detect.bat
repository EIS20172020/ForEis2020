
python ./tools/detect.py ^
	--classes ./data/runway.names ^
	--num_classes 1 ^
	--weights ./checkpoints/yolov3_train.tf ^
	--image ./data/runway4.jpg ^
    --yolo_score_threshold 0.001