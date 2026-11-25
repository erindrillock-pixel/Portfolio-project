# Detecting Phishing Websites from URL and Page Features

**Question:** Based on a set of features describing a website's URL, domain and page behaviour, can a model determine whether a site is phishing or legitimate, without missing many phishing sites?

**Dataset:** UCI *Phishing Websites* (id 327), CC BY 4.0. Mohammad, R. & McCluskey, L. (2012). *Phishing Websites* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51W2X. It is downloaded automatically from UCI on the first run (needs internet) and saved to `data/phishing_websites.csv`, which is not committed.

## Notebooks

Run them in this order:

1. `notebooks/data_baseline.ipynb` – data audit, cleaning, train/test split and majority-class baseline (Milestone 2)
2. `notebooks/model_comparison.ipynb` – logistic regression, k-NN, decision tree and random forest compared with the baseline using nested cross-validation, plots, error analysis and draft conclusion (Milestone 3). Takes about 2 minutes.

Results tables and figures are saved to `reports/` and `reports/figures/`.

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
```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/data_baseline.ipynb
jupyter nbconvert --to notebook --execute --inplace notebooks/model_comparison.ipynb
```
Or open them with `jupyter lab` and choose **Kernel → Restart Kernel and Run All Cells**.

## How to obtain Data

Nothing needs to be downloaded by hand. The first notebook (`data_baseline.ipynb`) calls `load_dataset()` in `src/data.py`, which:

1. downloads the official zip from UCI (`https://archive.ics.uci.edu/static/public/327/phishing+websites.zip`);
2. reads `Training Dataset.arff` inside it (11,055 rows, 30 features + `Result`);
3. renames the columns to snake_case and saves `data/phishing_websites.csv`.

To download it on its own, from the project root: `python -m src.data`

The CSV is not committed (see `.gitignore`) because it can be re-downloaded exactly; the CC BY 4.0 licence would allow it to be included with attribution.

## Coding

Every feature is coded by the dataset authors' rules as -1 (phishing-like), 0 (suspicious) or 1 (legitimate-like). Target `result`: -1 = phishing, 1 = legitimate. The notebooks recode it as `is_phishing` (1 = phishing).
