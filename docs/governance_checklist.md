# Governance Checklist — PPE Detection Model

## 1. Privacy & Consent

- [x] **No personally identifiable information (PII):** The dataset contains construction site images. Faces are incidental to PPE detection and are generally small/distant.
- [x] **Public imagery:** All images originate from publicly available photographs (Roboflow/Kaggle public dataset).
- [x] **No biometric processing:** The model detects PPE objects, not individual identities. No facial recognition or worker tracking is performed.
- [ ] **Deployment consideration:** If deployed on a real construction site, workers must be informed that computer vision monitoring is active. Consent should be obtained per local labor regulations (e.g., GDPR in EU, OSHA guidelines in US, local privacy laws).

## 2. Data Minimization

- [x] **Minimum data principle:** Only 10 predefined object classes are detected. No additional personal data is extracted.
- [x] **No raw image retention required:** In deployment, images can be processed in real-time and discarded. Only detection results (class + bounding box) need to be logged.
- [x] **Public training data:** No proprietary or private data was used for model training.

## 3. Limitations Statement — When NOT to Use This Model

This model should **NOT** be used:

- **As the sole safety compliance mechanism.** It is a supplementary monitoring tool, not a replacement for human safety officers.
- **For individual worker identification or tracking.** The model detects PPE presence/absence, not people's identities.
- **In low-light, night, or indoor conditions** without retraining — the dataset primarily contains well-lit daytime images.
- **For legal compliance evidence** without human verification. With 87.6% precision and 67.7% recall, the model will both miss real violations and occasionally flag false ones.
- **For vehicle safety monitoring** — the vehicle class has only 47.4% AP@50 and is not reliable.
- **In environments different from construction sites** (labs, hospitals, factories) without domain-specific fine-tuning.

## 4. Risk Note — False Negatives vs. False Positives

| Risk Type | Impact | Frequency | Mitigation |
|-----------|--------|-----------|------------|
| **False Negative** (missed PPE violation) | **HIGH** — A worker without PPE goes unflagged, risking injury | 32.3% of violations missed (recall = 0.677) | Lower confidence threshold for safety-critical "NO-" classes; combine with human inspection |
| **False Positive** (incorrect alert) | **LOW-MEDIUM** — Unnecessary alert causes fatigue and reduced trust | 12.4% of detections are incorrect (precision = 0.876) | Require human confirmation before any disciplinary action; use temporal smoothing (multiple frames) |

**Key principle:** In safety applications, false negatives are more dangerous than false positives. For deployment, the model should be tuned to favor **recall over precision** — it is better to over-alert than to miss a genuine safety violation.

## 5. License & Data Rights

### Project License
This project is released under the **MIT License**. See [LICENSE](../LICENSE).

### Dataset Rights
- **Dataset:** Construction Site Safety Image Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow) (originally from Roboflow)
- **Usage:** Public dataset, used for educational and research purposes
- **Redistribution:** Compliant with Kaggle's terms of use

### Model & Framework
- YOLOv8n architecture by [Ultralytics](https://github.com/ultralytics/ultralytics) (AGPL-3.0 license for the library)
- For commercial deployment, review Ultralytics licensing at https://ultralytics.com/license

---

*Last updated: February 2026*