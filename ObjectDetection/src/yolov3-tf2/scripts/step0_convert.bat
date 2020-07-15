<<<<<<< HEAD
@echo [Script] convert yolov3 pre-weights to tf
python ./tools/convert.py ^
    --output ./checkpoints/yolov3.tf ^
    --num_classes 80
python ./tools/convert.py ^
    --weights ./data/yolov3.weights ^
    --output ./checkpoints/yolov3.ckpt ^
=======
@echo [Script] convert yolov3 pre-weights to tf
python ./tools/convert.py ^
    --output ./checkpoints/yolov3.tf ^
    --num_classes 80
python ./tools/convert.py ^
    --weights ./data/yolov3.weights ^
    --output ./checkpoints/yolov3.ckpt ^
>>>>>>> a59cbc6eafb25f61d746572c4e39b6440eb3d535
    --num_classes 80