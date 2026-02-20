# PPE Detection on Construction Sites — Mini Report

**M4U3 Assignment · MSc AI for Architecture & Construction**
**Author:** Carlo Cogni · **Date:** February 2026

---

## Executive Summary

This project implements an automated Personal Protective Equipment (PPE) detection system for construction sites using YOLOv8n. The model detects 10 classes — hardhats, masks, safety vests (and their absence), people, safety cones, machinery, and vehicles — achieving **75.4% mAP@50** and **87.6% precision** after 30 training epochs on 2,605 images.

The system runs at **1.9 ms per image** on an RTX 4070 GPU (~500 FPS), making it suitable for real-time video monitoring. The entire pipeline is reproducible from a single Jupyter notebook with no local dataset management required (auto-downloads via KaggleHub).

## Results

### Quantitative Performance

| Metric | Value |
|--------|-------|
| Precision | 0.876 |
| Recall | 0.677 |
| mAP@50 | 0.754 |
| mAP@50-95 | 0.441 |
| F1 score | 0.76 @ conf 0.44 |

**Top performers:** machinery (91.0%), Safety Cone (85.9%), Mask (85.7%).
**Weakest:** vehicle (47.4%), NO-Mask (55.5%), NO-Hardhat (66.8%).

### Key Observations

The model shows a clear pattern: *detecting the presence* of PPE (Hardhat 84.1%, Mask 85.7%, Safety Vest 80.8%) is significantly easier than *detecting its absence* (NO-Hardhat 66.8%, NO-Mask 55.5%). This is expected — positive classes have distinctive visual features (colored helmet, reflective vest), while negative classes rely on confirming the absence of those features on small human body regions.

Training curves show all losses (box, cls, dfl) converging smoothly over 30 epochs, with mAP@50 still trending upward at epoch 30, suggesting additional epochs could yield further improvement.

## Limitations

1. **Recall gap (67.7%):** Nearly a third of PPE violations go undetected, particularly for NO-Mask (43% missed) and NO-Hardhat (38% missed). This is a critical limitation for a safety system.

2. **Vehicle detection is unreliable (47.4% AP@50):** Nearly half of vehicles are missed entirely. The class has few training examples and high visual diversity.

3. **Dataset bias:** Training data is primarily well-lit, daytime, outdoor construction sites. Performance will degrade in low-light, indoor, or non-standard environments.

4. **No temporal reasoning:** The model processes single frames independently. A momentary occlusion (turning head, bending down) can trigger false violations. Production systems should use multi-frame smoothing.

5. **Not a standalone safety system:** The 12.4% false positive rate and 32.3% false negative rate mean this tool must supplement — not replace — human safety oversight.

---

*Full results, training curves, error analysis, and governance documentation available in the [GitHub repository](https://github.com/CarloCogni/computer-vision-with-YOLO).*