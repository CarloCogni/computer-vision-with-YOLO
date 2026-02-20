# Segment Anything Model (SAM) Exploration

As part of the pipeline development for PPE detection, we explored Meta's Segment Anything Model (SAM) to evaluate its 
utility for automated annotation and precise pixel-level segmentation of construction site hazards.

### What Helped
* **Zero-Shot Segmentation for Distinct Objects:** SAM was highly effective at zero-shot segmenting strongly defined 
* objects like safety cones, large machinery, and high-visibility safety vests. When prompted with a rough bounding box,
* it generated highly accurate pixel masks, which could dramatically speed up the creation of future segmentation datasets.
* **Background Separation:** It excelled at separating foreground workers from complex scaffolding or dirt backgrounds, 
* provided the lighting contrast was sufficient.

### What Failed
* **Inference Speed:** SAM is significantly heavier and slower than YOLOv8n. While YOLO runs at ~1.9ms per image, 
* making it viable for live video feeds, SAM's inference time makes it impractical for real-time AECO deployment on 
* standard edge devices.
* **Ambiguous "Absence" Classes:** SAM struggles with negative classes (like `NO-Mask` or `NO-Hardhat`). Because SAM 
* segments *things*, asking it to segment the *absence* of a helmet often just resulted in segmenting a worker's hair
* or the background behind their head, adding no structural value to the detection pipeline.
* **Heavy Occlusion:** In crowded areas with overlapping workers, SAM's auto-segmentation occasionally merged multiple
* workers into a single mask or failed to isolate a hardhat partially obscured by pipes or shadows.