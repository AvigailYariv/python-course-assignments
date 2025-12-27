"""data_from_excel.py

Read mass-spec results from an Excel file, filter ribosomal proteins and inspect Coverage [%].

Usage:
    python data_from_excel.py [path/to/file.xlsx]

If no path is given the script will search the local "data/" folder for a .xlsx file (prefers
"sample_6.xlsx" if present).

Dependencies:
    pandas, numpy, matplotlib, openpyxl

Functions:
- load_excel(path)
- filter_ribosomal(df)
- parse_coverage(df, coverage_col="Coverage [%]")
- plot_histogram(coverage_series, bins=20, save_path=None)

"""
from typing import Optional, Union
from pathlib import Path
import sys
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_excel(path: Union[str, Path]) -> pd.DataFrame:
    """Load an Excel file into a DataFrame.

    The Excel file uses row 2 (1-based) as the header row (column names), so this function
    reads with header=1 by default.

    Raises FileNotFoundError or RuntimeError with actionable messages.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Excel file not found: {p}")
    try:
        # Read with header=1 so column names come from the second row of the sheet
        return pd.read_excel(str(p), sheet_name=0, header=1)
    except Exception as exc:
        msg = str(exc).lower()
        if "openpyxl" in msg or "missing optional dependency 'openpyxl'" in msg:
            raise RuntimeError(
                "Reading .xlsx files requires 'openpyxl'. Install it with: python -m pip install openpyxl"
            ) from exc
        raise RuntimeError(f"Failed to read Excel file '{p}': {exc}") from exc


def filter_ribosomal(df: pd.DataFrame, description_col: str = "Description") -> pd.DataFrame:
    """Return rows where description contains 'ribosomal' or 'Ribosome-binding' (case-insensitive).

    Raises KeyError if the description column is missing.
    """
    if description_col not in df.columns:
        # try to be helpful: look for a close match ignoring case
        cols_lower = [c.lower() for c in df.columns]
        if "description" in cols_lower:
            # find actual column name with exact match ignoring case
            idx = cols_lower.index("description")
            description_col = df.columns[idx]
        else:
            raise KeyError(f"Missing '{description_col}' column. Available columns: {df.columns.tolist()}")

    desc = df[description_col].astype(str)
    mask = desc.str.contains("ribosomal", case=False, na=False) | desc.str.contains("Ribosome-binding", case=False, na=False)
    return df[mask]


def parse_coverage(df: pd.DataFrame, coverage_col: str = "Coverage [%]") -> pd.Series:
    """Extract numeric coverage values (as floats) from `coverage_col`.

    Accepts values like '45%', '45.2', '45,2' and will coerce non-convertible entries to NaN.
    Raises KeyError if coverage column is missing.
    """
    if coverage_col not in df.columns:
        # try to find a plausible column name
        candidates = [c for c in df.columns if "coverage" in c.lower()]
        if candidates:
            coverage_col = candidates[0]
        else:
            raise KeyError(f"Missing '{coverage_col}' column. Available columns: {df.columns.tolist()}")

    raw = df[coverage_col].astype(str).str.strip()
    # Remove percentage sign and replace comma with dot
    cleaned = raw.str.replace("%", "", regex=False).str.replace(",", ".", regex=False)
    # Remove any non-numeric prefix/suffix while keeping decimal point and minus
    cleaned = cleaned.str.replace(r"[^0-9.\-]", "", regex=True)
    values = pd.to_numeric(cleaned, errors="coerce")
    return values


def plot_histogram(coverage_series: pd.Series, bins: int = 20, save_path: Optional[Union[str, Path]] = None) -> None:
    """Plot histogram of coverage values."""
    values = coverage_series.dropna().values
    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=bins, color="C2", edgecolor="black")
    plt.xlabel("Coverage [%]")
    plt.ylabel("Number of proteins")
    plt.title("Distribution of Coverage [%]")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved histogram to {save_path}")
    else:
        plt.show()


def summarize_series(s: pd.Series) -> str:
    """Return a short text summary of a numeric series."""
    return (
        f"count={int(s.dropna().shape[0])}, mean={s.mean():.2f}, median={s.median():.2f}, std={s.std():.2f}"
        if s.dropna().shape[0] > 0
        else "no numeric values"
    )


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv:
        path = Path(argv[0])
    else:
        # auto-detect a file in data/
        data_dir = Path(__file__).parent / "data"
        if not data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {data_dir}")
        candidates = list(data_dir.glob("*.xlsx"))
        if not candidates:
            raise FileNotFoundError(f"No .xlsx files found in {data_dir}")
        preferred = next((c for c in candidates if c.name == "sample_6.xlsx"), None)
        path = preferred or candidates[0]

    print("Using Excel file:", path.resolve())

    df = load_excel(path)
    print("Loaded sheet with shape:", df.shape)
    print("Columns:", df.columns.tolist())

    # Identify a name column (the first column is said to contain sample identifiers)
    name_col = df.columns[0]
    if name_col is None:
        raise KeyError("No columns found in the Excel file.")

    print("Using name column:", name_col)

    filtered = filter_ribosomal(df)
    print("Filtered to ribosomal proteins, rows:", filtered.shape[0])

    coverage = parse_coverage(filtered)
    print("Coverage summary:", summarize_series(coverage))

    # Histogram
    plot_histogram(coverage, bins=20, save_path=Path(__file__).parent / "coverage_histogram.png")


if __name__ == "__main__":
    main()
