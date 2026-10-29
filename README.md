# Detecting Phishing Websites from URL and Page Features

CT4101 Machine Learning Portfolio Project, University of Galway. Erin Drillock, Student ID: 26100644

**Question:** Given features describing a website's URL, domain and page behaviour, can a model reliably classify
the site as *phishing* or *legitimate*, without missing many phishing sites?

**Repository:** https://github.com/erindrillock-pixel/Portfolio-project

**Dataset:** UCI *Phishing Websites* (id 327), CC BY 4.0. Mohammad, R. & McCluskey, L. (2012).
https://doi.org/10.24432/C51W2X. See [`data/README.md`](data/README.md).

## Current status: Milestone 2 (data and baseline checkpoint)

`notebooks/01_data_audit_and_baseline.ipynb` contains:
- the data audit (shape, variable types, value ranges/outliers, missing values, duplicates, target distribution)
- the cleaning decisions (exact duplicates removed **before** splitting to prevent leakage)
- the evaluation design: stratified 80/20 hold-out test set (left untouched until the final evaluation), plus stratified 5-fold cross-validation on the training set
- the preprocessing pipeline (one-hot encoding inside a scikit-learn `Pipeline`)
- baseline results (majority-class `DummyClassifier`) for recall, precision, F1, ROC-AUC and accuracy

## Folder structure

```
.
├── README.md
├── requirements.txt
├── ASSISTANCE_DECLARATION.md
├── data/
│   └── README.md            
├── notebooks/
│   └── 01_data_audit_and_baseline.ipynb
├── src/
│   └── data.py              
└── reports/
    ├── baseline_cv_results.csv
    └── figures/             
```

## Setup

Tested with **Python 3.14** on macOS.

```bash
git clone https://github.com/erindrillock-pixel/Portfolio-project.git
cd Portfolio-project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

From the project root, either open the notebook interactively:

```bash
jupyter lab notebooks/01_data_audit_and_baseline.ipynb
```

and choose **Kernel → Restart Kernel and Run All Cells**, or run it non-interactively from top to bottom:

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/01_data_audit_and_baseline.ipynb
```

The first run downloads the dataset to `data/phishing_websites.csv`. The notebook then writes
`reports/baseline_cv_results.csv` and the figures in `reports/figures/`. All randomness uses a fixed seed (`RANDOM_STATE = 42`),
so the results are reproducible.

## Assistance

See [`ASSISTANCE_DECLARATION.md`](ASSISTANCE_DECLARATION.md).
