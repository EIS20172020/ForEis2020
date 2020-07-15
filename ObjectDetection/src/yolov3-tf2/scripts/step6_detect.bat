<<<<<<< HEAD

python ./tools/detect.py ^
	--classes ./data/runway.names ^
	--num_classes 1 ^
	--weights ./checkpoints/yolov3_train.tf ^
	--image ./data/runway4.jpg ^
=======

python ./tools/detect.py ^
	--classes ./data/runway.names ^
	--num_classes 1 ^
	--weights ./checkpoints/yolov3_train.tf ^
	--image ./data/runway4.jpg ^
>>>>>>> a59cbc6eafb25f61d746572c4e39b6440eb3d535
    --yolo_score_threshold 0.001