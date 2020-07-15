@echo [Script] convert yolov3 pre-weights to tf
python ./tools/convert.py ^
    --output ./checkpoints/yolov3.tf ^
    --num_classes 80
python ./tools/convert.py ^
    --weights ./data/yolov3.weights ^
    --output ./checkpoints/yolov3.ckpt ^
    --num_classes 80