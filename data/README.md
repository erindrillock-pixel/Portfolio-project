# Data

**Dataset:** Phishing Websites, UCI Machine Learning Repository, dataset id 327
**Page:** https://archive.ics.uci.edu/dataset/327/phishing+websites
**Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Citation:** Mohammad, R. & McCluskey, L. (2012). *Phishing Websites* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51W2X

## How to obtain it

The data is downloaded automatically from UCI the first time the notebook runs. To download it on its own:

```bash
python -m src.data
```

This downloads the official zip from the UCI dataset page
(`https://archive.ics.uci.edu/static/public/327/phishing+websites.zip`), reads `Training Dataset.arff` inside it
and saves it as `data/phishing_websites.csv` (11,055 rows, 30 feature columns + `result`). The column names are converted to snake_case, and the original
spelling errors (e.g. `Shortining_Service`) are corrected. The script prints the old -> new name of every column.

The CSV is not committed (see `.gitignore`) because it can be re-downloaded exactly. The licence would permit
redistribution with attribution if it ever needs to be included.

## Coding

All features are coded -1 (phishing-like), 0 (suspicious) or 1 (legitimate-like) by the dataset authors' rules.
Target `result`: -1 = phishing, 1 = legitimate. The notebook recodes this to `is_phishing` (1 = phishing).
