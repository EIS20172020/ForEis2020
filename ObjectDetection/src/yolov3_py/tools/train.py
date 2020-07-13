from absl import app, flags, logging
from absl.flags import FLAGS

import tensorflow as tf
import numpy as np
import cv2
import os
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny, YoloLoss,
    yolo_anchors, yolo_anchor_masks,
    yolo_tiny_anchors, yolo_tiny_anchor_masks
)
from yolov3_tf2.utils import freeze_all
import yolov3_tf2.dataset as dataset

flags.DEFINE_string('dataset', './data/VOC2012/', 'path to dataset')
flags.DEFINE_string('val_dataset', '', 'path to validation dataset')
flags.DEFINE_boolean('tiny', True, 'yolov3 or yolov3-tiny')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_enum('mode', 'fit', ['fit', 'eager_fit', 'eager_tf'],
                  'fit: model.fit, '
                  'eager_fit: model.fit(run_eagerly=True), '
                  'eager_tf: custom GradientTape')
flags.DEFINE_enum('transfer', 'none',
                  ['none', 'darknet', 'no_output', 'frozen', 'fine_tune'],
                  'none: Training from scratch, '
                  'darknet: Transfer darknet, '
                  'no_output: Transfer all but output, '
                  'frozen: Transfer and freeze all, '
                  'fine_tune: Transfer all and freeze darknet only')
flags.DEFINE_integer('size', 416, 'image size')
flags.DEFINE_integer('epochs', 2, 'number of epochs')
flags.DEFINE_integer('batch_size', 8, 'batch size')
flags.DEFINE_float('learning_rate', 1e-3, 'learning rate')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')
flags.DEFINE_integer('weights_num_classes', None, 'specify num class for `weights` file if different, '
                     'useful in transfer learning with different number of classes')


def main(_argv):
    # 使用gpu加速
    # tensorflow-gpu config
    physical_devices = tf.config.experimental.list_physical_devices(
        device_type='GPU')
    print(os.system('nvidia-smi'))
    if len(physical_devices) > 0:
        try:
            tf.config.experimental.set_memory_growth(physical_devices[0], True)
        except:
            print('\nno physical devices available!\n')

    # 加载模型
    # yolov3 or yolov3-tiny
    if FLAGS.tiny:
        model = YoloV3Tiny(FLAGS.size, training=True,
                           classes=FLAGS.num_classes)
        anchors = yolo_tiny_anchors
        anchor_masks = yolo_tiny_anchor_masks
    else:
        model = YoloV3(FLAGS.size, training=True, classes=FLAGS.num_classes)
        anchors = yolo_anchors
        anchor_masks = yolo_anchor_masks

    model.summary()

    # https://blog.csdn.net/DumpDoctorWang/article/details/84028957

    # 载入数据集
    if FLAGS.dataset:
        # 如果指定数据集
        train_dataset = dataset.load_tfrecord_dataset(
            FLAGS.dataset, FLAGS.classes, FLAGS.size)
    # 载入训练集
    if FLAGS.val_dataset:
        val_dataset = dataset.load_tfrecord_dataset(
            FLAGS.val_dataset, FLAGS.classes, FLAGS.size)

    val_dataset = val_dataset.batch(FLAGS.batch_size)
    val_dataset = val_dataset.map(lambda x, y: (
        dataset.transform_images(x, FLAGS.size),
        dataset.transform_targets(y, anchors, anchor_masks, FLAGS.size)))

    # 数据集乱序
    train_dataset = train_dataset.shuffle(buffer_size=512)
    # dataset的batch
    train_dataset = train_dataset.batch(FLAGS.batch_size)
    train_dataset = train_dataset.map(lambda x, y: (
        dataset.transform_images(x, FLAGS.size),
        dataset.transform_targets(y, anchors, anchor_masks, FLAGS.size)))
    train_dataset = train_dataset.prefetch(
        buffer_size=tf.data.experimental.AUTOTUNE)


    # 选择优化器
    optimizer = tf.keras.optimizers.Adam(lr=FLAGS.learning_rate)
    # 损失函数
    loss = [
        YoloLoss(anchors[mask], classes=FLAGS.num_classes)
        for mask in anchor_masks
    ]

    model.compile(
        optimizer=optimizer,
        loss=loss,
        run_eagerly=(FLAGS.mode == 'eager_fit')
    )

    checkpoint_save_path='./checkpoints/yolov3.ckpt'
    if os.path.exists(checkpoint_save_path+'.index'):
        model.load_weights(checkpoint_save_path)
        # 若成功加载前面保存的参数，输出下列信息
        print("     ===============  checkpoint_loaded ===============")

    callbacks = [
        tf.keras.callbacks.ReduceLROnPlateau(verbose=1),
        # 提早结束：当模型的损失不再下降的时候就终止训练，当然，会保存最优的模型。
        tf.keras.callbacks.EarlyStopping(patience=3, verbose=1),
        # 模型断点续训：保存当前模型的所有权重
        tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_save_path,
            verbose=1,
            save_weights_only=True,
            save_best_only=True),   
        # TensorBoard 可视化
        # command: tensorboard --logdir=./logs
        tf.keras.callbacks.TensorBoard(log_dir='logs')  ]


    history = model.fit(
        train_dataset,
        epochs=FLAGS.epochs,
        callbacks=callbacks,
        validation_data=val_dataset
    )

    h5_save_path = './checkpoints/model.h5'
    try:
        model.save(h5_save_path)
    except:
        print('cannot save model')
    else:
        print('save model in:',h5_save_path)


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
 