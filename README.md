# DSCI 552 HW3

Hongwei Xiao | GitHub: Ga9a

Open `notebooks/Xiao_Hongwei_HW3.ipynb` for the executed answers to 1(a)-(c) and ISLR 3.7.4(a)-(d).

## Run

Install the packages in `requirements.txt` with `python -m pip install -r requirements.txt`,
open the notebook in Jupyter or VS Code, select that Python environment, and run all cells.
Start from this directory or its `notebooks` directory. All data paths are relative.
The raw course-provided AReM data are included under `data/AReM`; no download is required.

## Results

- 88 instances; 69 training and 19 test instances using the specified file numbers.
- 42 features per instance; complete tables and split metadata in `results`.
- 90% percentile bootstrap intervals for all 42 feature standard deviations,
  using 10,000 resamples of 88 instances and seed 42.
- Three selected statistic types: mean, standard deviation, and maximum.

`bending2/dataset4.csv` uses spaces as delimiters. `sitting/dataset8.csv` contains
479 observations. The parser accepts both delimiters and uses the observed records
without imputation. Original input files are preserved.

Part 4 of the homework PDF is assigned to HW4; the optional practice questions are
not included. Sources and AI assistance are disclosed in the notebook.

## Reproducibility checks

Use Python 3.12 with the pinned dependencies. The submitted notebook preserves its recorded analysis; the verification script checks notebook structure and saved errors without changing it.

```sh
python scripts/verify_notebook.py
python scripts/verify_notebook.py --execute
```

Execution uses the notebook directory as its working directory, so dataset paths resolve consistently. Run the command in the environment where the requirements were installed. CI reruns all code cells on a clean checkout. Generated results written by notebook code may be refreshed during execution.
