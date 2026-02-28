# PPE Detection on Construction Sites — Mini Report

**M4U3 Assignment · MSc AI for Architecture & Construction**
**Author:** Carlo Cogni · **Date:** February 2026

---

## Phase 1: Version 1 (Baseline Performance)
### Executive Summary

This project implements an automated Personal Protective Equipment (PPE) detection system for construction sites using YOLOv8n. The model detects 10 classes — hardhats, masks, safety vests (and their absence), people, safety cones, machinery, and vehicles — achieving **75.4% mAP@50** and **87.6% precision** after 30 training epochs on 2,605 images.

The system runs at **1.9 ms per image** on an RTX 4070 GPU (~500 FPS), making it suitable for real-time video monitoring. The entire pipeline is reproducible from a single Jupyter notebook with no local dataset management required (auto-downloads via KaggleHub).

### Results

#### Quantitative Performance

| Metric | Value |
|--------|-------|
| Precision | 0.876 |
| Recall | 0.677 |
| mAP@50 | 0.754 |
| mAP@50-95 | 0.441 |
| F1 score | 0.76 @ conf 0.44 |

**Top performers:** machinery (91.0%), Safety Cone (85.9%), Mask (85.7%).
**Weakest:** vehicle (47.4%), NO-Mask (55.5%), NO-Hardhat (66.8%).

### Key Observation V1
* V1 demonstrated that *detecting the presence* of PPE was easier than *detecting its absence*. However, significant "label noise" in the unverified dataset led to unreliable vehicle detection (47.4% mAP) and potential alert fatigue in real-world scenarios.
* The model shows a clear pattern: *detecting the presence* of PPE (Hardhat 84.1%, Mask 85.7%, Safety Vest 80.8%) is significantly easier than *detecting its absence* (NO-Hardhat 66.8%, NO-Mask 55.5%). This is expected — positive classes have distinctive visual features (colored helmet, reflective vest), while negative classes rely on confirming the absence of those features on small human body regions.
* Training curves show all losses (box, cls, dfl) converging smoothly over 30 epochs, with mAP@50 still trending upward at epoch 30, suggesting additional epochs could yield further improvement.

---

## Phase 2: Version 2 (Audited & Optimized)

To address the quality gap in V1, a **Clean Seed Strategy** was implemented. This involved a 100% manual audit of 612 high-priority images to correct bounding box inaccuracies and eliminate label noise.

### Quantitative Performance (V2 Audited)
The following metrics represent the model's performance against verified ground truth:

| Class | mAP@50 | Recall | Strategic Impact |
| :--- | :--- | :--- | :--- |
| **Vehicle** | **0.663** | **1.00** | **Zero-miss heavy machinery detection** |
| **Hardhat** | **0.677** | **0.82** | **Stable head-protection monitoring** |
| **Safety Vest**| **0.535** | **0.79** | **Refined torso-level verification** |
| **Person** | **0.498** | **0.82** | **Consistent worker identification** |



### Key Improvements in V2
1. **Safety-Critical Reliability:** Vehicle detection reached **1.00 recall**, ensuring the system never misses heavy machinery in worker proximity zones.
2. **Data Integrity:** By reducing the dataset to a "Clean Seed" of 612 audited images, the model learned high-quality features rather than memorizing noisy labels.
3. **Deployment Speed:** Maintained an inference latency of **3.0 ms** on an NVIDIA Tesla T4, supporting high-speed CCTV integration.

---

## Current Limitations & Future Work

While Version 2 significantly improves data integrity, technical challenges remain for future development:

1. **Background Leakage:** The model incorrectly flags background site elements (scaffolding/poles) as "Person" at a **26% error rate**. 
2. **Classification Ambiguity:** A **9% misclassification rate** exists between Hardhats and Masks due to spatial proximity in the "head" region.
3. **Recall Gap in PPE Absence:** Detecting the *absence* of PPE (NO-Mask/NO-Hardhat) remains significantly more difficult than detecting presence due to the smaller pixel footprint of bare heads/faces.
4. **Dataset Bias:** Performance is optimized for daytime, outdoor site conditions. Performance may degrade in low-light or indoor concrete shells.
5. **No Temporal Reasoning:** Production deployment should utilize multi-frame smoothing to prevent false alerts caused by momentary occlusions.

---

*Full results, training curves, error analysis, and governance documentation available in the [GitHub repository](https://github.com/CarloCogni/computer-vision-with-YOLO).*
