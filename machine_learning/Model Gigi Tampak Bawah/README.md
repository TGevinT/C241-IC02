# Table Machine Learning Gigi Tampak Bawah

| Version       | Augmentation                                                   | Accuracy | Val Accuracy |
|---------------|----------------------------------------------------------------|----------|--------------|
| Xception      | rescale = 1/225                                                | 0.9993   | 0.9545       |
| Xception      | rescale=1/255<br>rotation range=20<br>width shift range=0.2<br>height shift range=0.2<br>shear range=0.2<br>zoom range=0.2<br>horizontal flip=True<br>fill mode='nearest' | 0.9966   | 0.9432       |
| InceptionV3   | rescale=1/255<br>rotation range=20<br>width shift range=0.2<br>height shift range=0.2<br>shear range=0.2<br>zoom range=0.2<br>horizontal flip=True<br>fill mode='nearest' | 0.9849   | 0.9403       |
| VGG16         | rescale=1/255<br>rotation range=20<br>width shift range=0.2<br>height shift range=0.2<br>shear range=0.2<br>zoom range=0.2<br>horizontal flip=True<br>fill mode='nearest' | 0.9866   | 0.9247       |
| YoloV8s       | imgsz = 640                                                    | 1        | 0.973        |
| YoloV8x       | imgsz = 224                                                    | 1        | 0.970        |
| YoloV8n       | imgsz = 224                                                    | 1        | 0.965        |
| YoloV8n       | imgsz = 640                                                    | 1        | 0.973        |
