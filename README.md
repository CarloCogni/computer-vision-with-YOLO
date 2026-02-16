# [Project Name] - AECO Object Detection

## Problem & Success Criteria
* **Problem:** [One sentence description, e.g., Detecting safety helmets on construction sites to improve compliance.]
* **Success Criteria:** [e.g., mAP50 > 80% on validation set.]

## Dataset
* **Link:** [Insert your Roboflow Universe Link Here]
* **Split:** 80% Train / 10% Valid / 10% Test
* **Classes:** [List classes, e.g., Helmet, Vest, No-Helmet]

## How to Reproduce (Google Colab)
1.  Open `notebooks/01_training_and_eval.ipynb` in Google Colab.
2.  Set Runtime to **GPU** (T4 is sufficient).
3.  Run all cells.
    * **Note:** If training takes too long, skip the `model.train()` cell and run the `model.load()` cell using the weights linked below.

## Results Summary
* **mAP50:** [TBD]
* **Precision:** [TBD]
* **Recall:** [TBD]
* **Key Takeaway:** [e.g., The model struggles with dark lighting conditions.]

## Reproducibility Checklist
* **Dataset Version:** v1 (Roboflow)
* **Model Variant:** YOLOv8n (Nano)
* **Epochs:** [e.g., 50]
* **Image Size:** [e.g., 640]
* **Ultralytics Version:** 8.x.x