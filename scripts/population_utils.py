\
from __future__ import annotations

import re
import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).strip().lower() for c in out.columns]
    return out


def build_population_65_plus(df: pd.DataFrame) -> pd.DataFrame:
    """
    Try to derive a municipality-level 65+ population table from the INE file.
    The exact file layout may need one manual adjustment after inspection.
    """
    df = normalize_columns(df)

    muni_col = next((c for c in df.columns if "mun" in c or "municip" in c), None)
    age_col = next((c for c in df.columns if "edad" in c or c == "age"), None)
    value_col = next((c for c in df.columns if c in {"valor", "value", "population", "poblacion", "población"}), None)

    # Long format
    if muni_col and age_col and value_col:
        ages = pd.to_numeric(df[age_col].astype(str).str.extract(r"(\d{1,3})")[0], errors="coerce")
        temp = df.assign(age_num=ages)
        temp = temp.loc[temp["age_num"].ge(65)]
        out = (
            temp.groupby(muni_col, as_index=False)[value_col]
            .sum()
            .rename(columns={muni_col: "mun_code", value_col: "pop_65_plus"})
        )
        return out

    # Wide format with ages in columns
    age_cols = [c for c in df.columns if re.search(r"(^|\D)(6[5-9]|[7-9]\d|100)(\D|$)", c)]
    if age_cols:
        id_cols = [c for c in df.columns if c not in age_cols]
        out = df[id_cols].copy()
        out["pop_65_plus"] = df[age_cols].apply(pd.to_numeric, errors="coerce").sum(axis=1)
        if muni_col and muni_col in out.columns:
            out = out.rename(columns={muni_col: "mun_code"})
        return out

    raise ValueError(
        "Could not parse age structure from the population file. "
        "Inspect the raw dataframe and adapt the parser to the published layout."
    )
