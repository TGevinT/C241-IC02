# Table Machine Learning Gigi Tampak Depan


| Version          | Augmentation                                                   | Accuracy | Val Accuracy |
|------------------|----------------------------------------------------------------|----------|--------------|
| InceptionV3      | rotation_range=20<br>width_shift_range=0.2<br>height_shift_range=0.2<br>shear_range=0.2<br>zoom_range=0.2<br>horizontal_flip=True<br>fill_mode='nearest'<br>brightness_range=[0.5, 1.5] | 0.9967   | 0.98346      |
| HYPERPARAMETER TUNER | rescale=1/255<br>fill_mode='nearest'                            | 0.9961   | 0.9478       |
| CNN              | rescale=1/255                                                  | 0.9678   | 0.9302       |
| EFFICIENTNETV2 B3| rescale=1/255,<br>validation_split=0.2,<br>fill_mode='nearest' | 0.9905   | 0.8624       |
| YoloV8s          | imgsz=640                                                       | 1        | 0.986        |


### Untuk data h.5 terdapat [di drive](https://drive.google.com/drive/folders/1Y1RjevTpn7bTu_9GHUaRpYOHy2325x12?usp=sharing)

