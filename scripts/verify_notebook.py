"""Validate the submitted notebook and optionally rerun every code cell."""
import argparse
from pathlib import Path
import nbformat
from nbclient import NotebookClient

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--execute", action="store_true", help="Execute every cell using the current Python environment")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
notebooks = list((root / "notebooks").glob("*.ipynb"))
if len(notebooks) != 1:
    raise SystemExit("Expected one submitted notebook")
path = notebooks[0]
notebook = nbformat.read(path, as_version=4)
nbformat.validate(notebook)
if args.execute:
    NotebookClient(notebook, timeout=600, kernel_name="python3",
                   resources={"metadata": {"path": str(path.parent)}}).execute()
errors = [output for cell in notebook.cells if cell.cell_type == "code"
          for output in cell.get("outputs", []) if output.output_type == "error"]
if errors:
    raise SystemExit("Notebook contains cell execution errors")
print(f"Verified {path.name}" + (" and executed every code cell" if args.execute else " format and saved outputs"))
