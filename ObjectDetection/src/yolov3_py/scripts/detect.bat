@echo detect from images
python ./tools/detect.py ^
	--classes ./data/fire_voc2012.names ^
	--num_classes 20 ^
	--weights ./checkpoints/yolov3.tf ^
	--image ./data/fire.jpg

