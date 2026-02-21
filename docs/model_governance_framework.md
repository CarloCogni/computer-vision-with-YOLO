# Safety-AI Governance Framework

## 1. Data Privacy & Consent
* **Minimization Strategy:** The study employs a **"Purpose-Specific"** data collection policy. No biometric or personally identifiable information (PII) is extracted; the neural network's focus is mathematically restricted to PPE compliance classes.
* **On-Site Consent:** It is established that all training data sourced from active construction sites adheres to standard site-entry privacy agreements and corporate safety monitoring protocols.
* **Anonymization Protocol:** During inference, any detected human biometric features (faces) are treated as secondary noise. For production-scale deployment, we recommend an automated Gaussian blur layer on face-regions to maintain **GDPR "Privacy by Design"** standards.

---

## 2. Operational Limitations (Constraints of Use)
* **Environmental Constraints:** This model was trained on high-visibility, clear-weather daytime data. Performance parity is **not guaranteed** in extreme weather (heavy fog, rain) or night-shift conditions without targeted dataset expansion.
* **Geometric & Distance Limits:** Reliability significantly degrades for subjects located **>20m** from the optical sensor. This is due to the *Feature Resolution Limit* inherent in the 640x640 input tensor.
* **Mission-Critical Safety:** This system is classified as an **Auditing & Analytics Tool**, not a real-time life-safety trigger. It is designed to complement, not replace, manual safety oversight in high-risk zones (e.g., heavy machinery swing paths).

---

## 3. Risk Management: The Safety Bias
* **Risk Taxonomy:** In the AECO sector, we operate under a **Safety-First Bias**. A *False Negative (FN)*—missing a non-compliant worker—represents a high-severity safety risk. A *False Positive (FP)*—misidentifying equipment as PPE—is a low-severity operational noise.
* **Optimization Strategy:** We intentionally prioritize **Recall over Precision** for all "NO-PPE" classes. Our objective is to minimize the probability of a missed safety violation, accepting a higher margin of "phantom" alerts as a necessary trade-off for site integrity.

---

## 4. Licensing & Data Rights
* **Software License:** The computational logic and notebook implementation are released under the **MIT License**.
* **Dataset Intellectual Property:** The PPE dataset is a hybrid of public research repositories and project-specific annotations. It is restricted to **Academic and Internal Use Only**; commercial redistribution is prohibited without explicit consent from the data owners.
