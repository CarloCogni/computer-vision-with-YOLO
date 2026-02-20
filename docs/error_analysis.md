# Error Analysis

## False Positives (Model detected something that is not there)

### FP-1: Safety Cone confused with NO-Safety Vest
**What:** The model occasionally labels orange/red objects (buckets, barriers) as "Safety Cone" even when they are not cones.
**Why:** Safety cones share a similar color profile (bright orange) with many other construction site objects. The model relies heavily on color cues rather than shape, leading to false triggers on similarly colored objects.

### FP-2: Hardhat detected on construction equipment
**What:** The model sometimes detects "Hardhat" on rounded features of machinery (e.g., headlights, tank caps).
**Why:** The model has learned that small, rounded, brightly colored objects near the top of frames are likely hard hats. Machinery components with similar visual signatures (circular, colored) trigger false detections.

### FP-3: Person detected in reflections or posters
**What:** Reflections in glass surfaces or safety posters showing workers are occasionally detected as "Person" with PPE annotations.
**Why:** The model cannot distinguish between real workers and their reflections or printed images. The visual features (human silhouette, clothing) are the same in both cases.

---

## False Negatives (Model missed something that is there)

### FN-1: Small/distant workers missed entirely
**What:** Workers far from the camera (occupying <30px in the image) are frequently missed — no detection at all.
**Why:** At 640px input resolution, very small objects lose critical features. YOLOv8n's nano architecture has limited feature extraction capacity for tiny objects. The dataset also has fewer examples of very distant workers.

### FN-2: NO-Hardhat missed in crowded scenes
**What:** In images with 5+ workers, some workers without hard hats are not flagged as "NO-Hardhat."
**Why:** Dense scenes cause NMS (Non-Maximum Suppression) to filter overlapping boxes. When workers are close together, the model suppresses weaker detections, sometimes removing correct NO-Hardhat predictions.

### FN-3: Workers partially occluded by machinery
**What:** Workers partially hidden behind machinery or scaffolding are not detected.
**Why:** Heavy occlusion (>50% of the body hidden) removes the visual cues the model relies on. The training set has limited examples of heavily occluded workers, so the model hasn't learned to handle these cases well.

---

## Prioritized Next Data Improvements

### 1. Add more small-object training data
**Action:** Collect or augment images with distant workers (>15m from camera). Apply mosaic augmentation or random crop-and-resize to create more small-object training examples. This directly addresses FN-1.

### 2. Increase crowded-scene representation
**Action:** Source images with 5+ workers in frame, especially with mixed PPE compliance. Ensure annotations are tight and non-overlapping. Consider tuning NMS IoU threshold (lower to 0.4) to retain more detections. This addresses FN-2.

### 3. Add hard negative mining for color-similar objects
**Action:** Explicitly add images of orange/red non-cone objects (buckets, barriers, signs) with no "Safety Cone" label, and images of round machinery components with no "Hardhat" label. This forces the model to learn shape discrimination and addresses FP-1 and FP-2.
