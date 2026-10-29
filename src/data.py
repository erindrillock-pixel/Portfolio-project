import io
import zipfile
from pathlib import Path
import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "phishing_websites.csv"
UCI_ZIP_URL = "https://archive.ics.uci.edu/static/public/327/phishing+websites.zip"
ARFF_NAME = "Training Dataset.arff"   
FEATURE_NAMES = [
    "having_ip_address", "url_length", "shortening_service", "having_at_symbol",
    "double_slash_redirecting", "prefix_suffix", "having_sub_domain",
    "ssl_final_state", "domain_registration_length", "favicon", "port",
    "https_token", "request_url", "url_of_anchor", "links_in_tags", "sfh",
    "submitting_to_email", "abnormal_url", "redirect", "on_mouseover",
    "right_click", "popup_window", "iframe", "age_of_domain", "dns_record",
    "web_traffic", "page_rank", "google_index", "links_pointing_to_page",
    "statistical_report",
]
TARGET_NAME = "result"
def parse_arff(text: str) -> pd.DataFrame:
    attributes, rows, in_data = [], [], False
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        lower = line.lower()
        if not in_data and lower.startswith("@attribute"):
            attributes.append(line.split()[1])
        elif lower.startswith("@data"):
            in_data = True
        elif in_data:
            rows.append([int(v) for v in line.split(",")])
    return pd.DataFrame(rows, columns=attributes)
    
def download_dataset(path: Path = DATA_PATH) -> Path:
    response = requests.get(UCI_ZIP_URL, timeout=60)
    response.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        arff_file = next(n for n in z.namelist() if n.endswith(ARFF_NAME))
        df = parse_arff(z.read(arff_file).decode("utf-8", errors="replace"))
    expected_cols = len(FEATURE_NAMES) + 1
    if df.shape[1] != expected_cols:
        raise ValueError(f"Expected {expected_cols} columns, got {df.shape[1]}")
    print("Renaming UCI columns (original -> project name):")
    for original, new in zip(df.columns, FEATURE_NAMES + [TARGET_NAME]):
        print(f"  {original:30s} -> {new}")
    df.columns = FEATURE_NAMES + [TARGET_NAME]
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved {df.shape[0]} rows to {path}")
    return path
    
def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        print(f"{path} not found - downloading from UCI...")
        download_dataset(path)
    df = pd.read_csv(path)
    expected = FEATURE_NAMES + [TARGET_NAME]
    if list(df.columns) != expected:
        raise ValueError("CSV columns do not match the expected names; delete it and re-run.")
    return df
    
if __name__ == "__main__":
    download_dataset()
