python -u ./tools/convert.py ^
    --weights ./data/yolov3-tiny.weights ^
    --tiny ^
    --output ./checkpoints/yolov3-tiny.tf ^
    --num_classes 80