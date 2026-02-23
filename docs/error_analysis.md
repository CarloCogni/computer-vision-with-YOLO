# Error Analysis & Failure Taxonomy

## False Positives (Type I Error)
*Model detected PPE where none physically exists.*

### FP-1: Semantic Confusion (Equipment as PPE)
* **What:** The model occasionally labels yellow excavator buckets, safety cones, or orange barriers as "Hardhat" or "Vest."
* **Why:** **Color-Overweighting.** The model is prioritizing high-visibility color features over specific hemispherical or torso-aligned geometry. In AECO environments, this results in "phantom" workers being detected on stationary equipment.

### FP-2: Background Noise (Luminance & Reflections)
* **What:** High-reflectivity surfaces (glass cladding or metallic scaffolding) are sometimes detected as "Vest."
* **Why:** **Specular Reflection Interference.** High-luminance reflections mimic the visual signature of retroreflective safety strips. The model lacks a "Context Filter" to distinguish between a biological worker and a reflective architectural surface.

### FP-3: Spatial Logic Failure (Geometry Misidentification)
* **What:** Rounded objects carried by workers (like circular buckets or lids) are detected as "Hardhats."
* **Why:** **Geometric Bias.** The model has learned to trigger a "Hardhat" detection for any hemispherical shape at the top of a detected cluster. Without a human skeleton constraint, it cannot differentiate between a helmet on a head and an object held in hands.

---

## False Negatives (Type II Error)
*Model missed PPE that was physically present.*

### FN-1: Small Object Detection Gap (Gloves)
* **What:** Workers wearing gloves at distances >10m are frequently missed by the model.
* **Why:** **Feature Resolution Limit.** In a 640x640 frame, gloves occupy a negligible pixel area. During the neural network's downsampling (convolution), these fine-grained features are "averaged out" and lost before reaching the prediction head.

### FN-2: Partial Occlusion (Construction Clutter)
* **What:** Workers standing behind pallets, machinery, or rebar are not flagged for wearing a "Vest."
* **Why:** **Feature Fragmentation.** The model expects a complete "shoulder-to-waist" silhouette. When >40% of the PPE is occluded by site clutter, the mathematical confidence score drops below the detection threshold.

### FN-3: Luminance Sensitivity (Shadows & Low Light)
* **What:** Workers in shaded trenches, indoor concrete shells, or night shifts show very low recall.
* **Why:** **Contrast Deficiency.** Dark PPE (black gloves or dust-covered vests) blends into the shadows. The model cannot define the bounding box boundaries because the pixel intensity of the object is too similar to the background noise.

---

## Prioritized Next Data Improvements

### 1. Implement Tiling Preprocessing
**Action:** Use a "Slicing" export in Roboflow to divide 4K site images into smaller 640x640 tiles. This effectively increases the resolution of small objects (Gloves) relative to the frame, directly addressing **FN-1**.

### 2. Hard Negative Mining (Zero-Label Injection)
**Action:** Add 100+ images containing site clutter (buckets, netting, cones) with **zero annotations**. This teaches the model that these specific high-visibility objects are "Background" and not PPE, reducing **FP-1** and **FP-3**.

### 3. Contrast-Robust Augmentations
**Action:** Retrain the model using a heavy "Mosaic" augmentation combined with "Random Brightness/Exposure" filters. This simulates the harsh lighting transitions found on construction sites, improving robustness for **FN-3**.****
