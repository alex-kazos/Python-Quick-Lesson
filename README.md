# 12-Week Python Programmer Mentorship

This is a structured path for helping a beginner become a practical Python programmer. Git and GitHub are included every week because they are professional habits, but the main story is programming skill:

1. Python fundamentals
2. Project habits
3. Data analysis with pandas
4. Data wrangling
5. Machine learning basics
6. AI engineering basics
7. A final capstone they can show

Every week should end with a working result, a commit, and one visible thing they can explain.

## Weekly Format

Each week has the same shape:

- `README.md`: session plan, mentor prompts, homework, and Git habit
- runnable script or notebook
- small data files where needed
- `solutions/`: one possible completed homework result
- a clear "done means" checklist

Use the weekly material as a teaching spine, not a lecture script. The session should feel like building together.

## Curriculum Map

| Week | Theme | Main Skill | Notebook | Script/App |
| --- | --- | --- | --- | --- |
| 01 | Python setup | variables, input, strings, numbers | `week_01_python_setup/python_setup_lab.ipynb` | `profile_app.py` |
| 02 | Control flow | conditions, loops, lists | `week_02_control_flow/control_flow_lab.ipynb` | `guess_the_number.py` |
| 03 | Functions and modules | parameters, returns, organization | `week_03_functions_and_modules/functions_lab.ipynb` | `expense_tracker.py` |
| 04 | Files and JSON | persistence, dictionaries, paths | `week_04_files_json_data/files_json_lab.ipynb` | `todo_app.py` |
| 05 | APIs | requests, JSON, documentation | `week_05_apis_and_requests/apis_lab.ipynb` | `weather_app.py` |
| 06 | Debugging and tests | tracebacks, pytest, safety | `week_06_debugging_and_tests/debugging_tests_lab.ipynb` | `calculator.py`, `test_calculator.py` |
| 07 | pandas basics | DataFrames, filtering, grouping | `week_07_pandas_basics/pandas_basics.ipynb` | sample CSV |
| 08 | Data wrangling | cleaning messy data | `week_08_data_wrangling/wrangling_lab.ipynb` | messy CSV |
| 09 | ML basics | features, labels, train/test | `week_09_ml_basics/ml_basics.ipynb` | student score CSV |
| 10 | ML project review | metrics, model card, refactor | `week_10_ml_project_review/ml_project_review.ipynb` | `model_training.py` |
| 11 | AI engineering | prompts, evals, retrieval, app shape | `week_11_ai_engineering_basics/ai_engineering_lab.ipynb` | RAG demo, Streamlit app |
| 12 | Capstone | portfolio, README, next path | `week_12_capstone_portfolio/portfolio_review.ipynb` | `capstone_plan.md` |

## Setup

Create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run a script:

```powershell
python week_01_python_setup/profile_app.py
```

Open notebooks:

```powershell
jupyter lab
```

Open a specific weekly notebook:

```powershell
jupyter lab week_07_pandas_basics/pandas_basics.ipynb
```

Run tests:

```powershell
pytest week_06_debugging_and_tests
```

Run the Week 11 app:

```powershell
streamlit run week_11_ai_engineering_basics/streamlit_app.py
```

## Using Solutions

Each weekly folder has a `solutions/` folder. Use it as an answer key after the student has tried the homework.

Good flow:

1. Let them attempt the homework first.
2. Ask them to explain their approach.
3. Compare with the solution.
4. Discuss tradeoffs instead of treating the solution as the only correct answer.

## Capstone Examples

The [capstone_examples](capstone_examples/README.md) folder contains one small working example for every capstone idea in [docs/capstone_options.md](docs/capstone_options.md).

These are intentionally small starter versions. They show what an MVP could look like before the student personalizes and expands one idea.

## Mentor Rule

Ask questions that teach thinking:

- "What do you expect this line to do?"
- "What changed after we ran it?"
- "What is the smallest next step?"
- "How would you debug this if I was not here?"
- "What would make this easier for future you?"
