| Model       | Version  | Augmentation                                | Accuracy | Val Accuracy |
|-------------|----------|---------------------------------------------|----------|--------------|
| CNN         | CNN      | rescale=1/255, rotation_range=20, fill_mode='nearest' | 0.99     | 0.80         |
| Inception V3| Inception V3| rescale=1/255, rotation_range=20, fill_mode='nearest' | 0.99     | 0.88         |
| Xception    | Pre-Trained | rescale=1/255, rotation_range=20, fill_mode='nearest' | 0.94     | 0.88         |
| YoloV8n*    | YoloV8n* | imgsz=640                                   | 1        | 0.98         |
| YoloV8s*    | YoloV8s* | imgsz=640                                   | 1        | 0.953        |
