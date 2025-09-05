import html
import math
import pathlib

import cogent3


def sanitize_text(text: str) -> str:
    return html.escape(text[:30]).replace("\n", " ")

def format_bytes(num_bytes: float) -> str:
    if math.isnan(num_bytes):
        return str(num_bytes)

    if num_bytes < 1024:
        return f"{num_bytes:,.1f} B"
    if num_bytes < 1024**2:
        return f"{num_bytes / 1024:,.1f} KB"
    if num_bytes < 1024**3:
        return f"{num_bytes / 1024**2:,.1f} MB"
    return f"{num_bytes / 1024**3:,.1f} GB"


def format_col(value):
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)


col_templates = {
    "mean(time) minutes": format_col,
    "std(time) minutes": format_col,
    "std(RAM) bytes": format_col,
    "mean(RAM)": format_bytes,
    "Result Type": sanitize_text,
}


def select_path(*parts) -> pathlib.Path | None:
    paths = list(pathlib.Path("../results").glob("**/*.tsv"))
    parts = set(parts)
    for p in paths:
        if parts.issubset(p.parts):
            return p
    return None


def display_results_for(*parts):
    path = select_path(*parts)
    if path is None:
        print(f"No results found for {parts}")
        return None
    table = cogent3.load_table(
        path,
        digits=2,
        column_templates=col_templates,
    )
    table.set_repr_policy(show_shape=False)
    return table
