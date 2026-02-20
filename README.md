# Real-Time PPE Detection for Construction Sites

## AECO Problem & Success Criteria
In complex EPC (Engineering, Procurement, and Construction) environments, manual safety compliance monitoring is labor-intensive and prone to human error. Unnoticed PPE (Personal Protective Equipment) violations can lead to severe accidents and legal liabilities. The goal of this project is to automate the detection of workers and their compliance with hardhat, mask, and safety vest protocols. 

**Success Criteria:** A lightweight model capable of real-time inference (>30 FPS) on edge devices or standard GPUs, achieving high precision to avoid false alarms that cause alert fatigue, while maintaining a recall high enough to act as a reliable supplementary safety tool.

## Class List & Labeling Rules
The model is trained to detect 10 distinct classes:
* **Person:** Any visible human figure on site.
* **Hardhat / NO-Hardhat:** Indicates whether a detected person's head is covered by a safety helmet or bare.
* **Mask / NO-Mask:** Indicates the presence or absence of a face mask.
* **Safety Vest / NO-Safety Vest:** Indicates whether a person's torso is covered by a high-visibility vest.
* **Safety Cone:** Orange/red traffic and safety cones.
* **machinery:** Heavy construction equipment (e.g., excavators, loaders).
* **vehicle:** Standard site vehicles (e.g., pickup trucks, vans).

## Dataset
* **Source:** Construction Site Safety Image Dataset (via Kaggle/Roboflow)
* **Split:** 80% Training / 20% Validation
* **Link:** [Insert your dataset link here]

## Reproducibility Checklist
* **Dataset Version:** [Insert Version/Date]
* **Model Variant:** YOLOv8n (Nano)
* **Hyperparameters:** 30 Epochs | Batch Size: [Insert Size, e.g., 16] | Image Size: 640x640
* **Environment:** `ultralytics==[Insert version number]`

## Reproducibility Proof
* **Last Successful Run:** February 20, 2026
* **Hardware Used:** NVIDIA RTX 4070 GPU
* **Expected Runtime:** ~[Insert minutes] minutes for full training; ~1.9 ms per image for inference.

## How to Reproduce (Colab)
1. Open the [Baseline/Training Notebook](link-to-your-notebook.ipynb) directly in Google Colab.
2. Ensure your runtime is set to GPU (Runtime > Change runtime type > T4 GPU or higher).
3. Click **Restart runtime** and then **Run all**.
4. The notebook is configured to automatically download the dataset via KaggleHub and install necessary dependencies.
5. **Note on Weights:** The trained weights from our 30-epoch run are saved in the repository at `./results/best.pt`. If you wish to skip training and only run inference, you can load these weights directly in the evaluation cell.

## Results Summary
After 30 epochs on 2,605 images, the model achieved:
* **mAP@50:** 0.754
* **Precision:** 0.876
* **Recall:** 0.677
* **Key Takeaways:** 1. Detecting the *presence* of PPE is highly accurate, but detecting its *absence* (especially NO-Mask and NO-Hardhat) struggles due to the small pixel footprint of bare heads/faces at a distance.
    2. Vehicle detection underperforms (47.4% mAP@50) due to high visual diversity and severe occlusion on active sites.
    3. The model is highly efficient, running at ~500 FPS on an RTX 4070, making it highly suitable for live CCTV streams.

## Deliverables & Documentation
* [Mini Report & Slides](./docs/mini_report.md)
* [Error Analysis](./docs/error_analysis.md)
* [Governance Checklist](./docs/governance_checklist.md)
* [SAM Exploration Notes](./docs/sam_exploration.md)
* **Trained Weights:** [GitHub Release (v1.0 / untagged)](https://github.com/CarloCogni/computer-vision-with-YOLO/releases/download/V1.0/best.pt)
* 
## How to Reproduce (Colab)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CarloCogni/computer-vision-with-YOLO/blob/main/notebooks/MAICEN1125_M4U3_train_and_evaluate.ipynb)
1. Click the **Open In Colab** badge above to load the training/inference notebook directly in your browser.
2. Ensure your runtime is set to GPU (**Runtime** > **Change runtime type** > **T4 GPU** or higher).
3. Click **Runtime** > **Restart and run all**.
4. The notebook is fully automated: it will download the 2,605-image dataset via KaggleHub and install all necessary 
    dependencies (like `ultralytics`).
5. **Note on Weights:** By default, the notebook will automatically download our pre-trained weights (`best.pt`) from 
    the latest GitHub Release and use them for inference to save time. If you wish to run the full 30-epoch training 
    from scratch, change `LOAD_PRETRAINED = False` in the configuration cell before running.



