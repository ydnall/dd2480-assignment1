# DD2480: Assignment 1 - Launch Interceptor Program

This repository contains the implementation of the DECIDE program and its tests.

This “Launch Interceptor Program” determines whether an interceptor should be launched based upon input radar tracking information.
The main mechanism of the LIC is the DECIDE()-function, which will output a launch decision, "YES" or "NO", based on the input data. Given up to 100 planar data points and a set of parameters, the program evaluates 15 Launch Interceptor Conditions (LIC0–LIC14), combines them using the Logical Connector Matrix (LCM) and Preliminary Unlocking Vector (PUV), and produces the final LAUNCH decision along with intermediate results (CMV, PUM, FUV) for transparency and testing.

## Requirements

- Python 3.10+

## Run program

There are two supported ways to run the code.
First, you can use Docker from the repository root to build and run a containerized version of the project.

### 1. Quick start (Docker)

```
docker build -t dd2480 .
docker run --rm dd2480
```

Second, you can run locally using a Python virtual environment. From inside assignment1/, create and activate a venv, install dependencies, and run the tests:

### 2. Local setup (venv)

```
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## Run tests (venv)

```
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## CI

GitHub Actions runs tests and linting on pushes and pull requests to `main` using Python 3.10.

## Statement of contributions

- Sumeya Yasir Isse: Made the solutions and ran tests for LIC 3, 4, 5; implemented FUV.

- Yiqin Lin: Made the solutions and ran tests for LIC 9, 10, 11; wrote README/documentation.

- Emma Lindblom: Made the solutions and ran tests for LIC 6, 7, 8; organized group and kept track of grading criteria.

- Andy Li: Made the solutions and ran tests for LIC 12, 13, 14; implemented CMV, **init**.py, and the top-level decide integration.

- Martin Zivojinovic: Made the solutions and ran tests for LIC 0, 1, 2; implemented PUM.

## Way of working (Essence self-assessment)

- We structured the work using GitHub Issues and feature branches. Each Launch Interceptor Condition (LIC) was tracked as its own issue, and each member implemented their assigned LIC(s) on a separate branch linked to that issue. Changes were integrated through pull requests, which required other group members to review before merging into the main branch.
  This helped keep the main branch clean and ensured that each merge represented a small, traceable change (an atomic commit). With the discussions and review history preserved in its corresponding PR.

Right now, we consider our way of working to be “in place”: we delegate clear tasks from the start, and we integrate regularly through reviewed PRs. To move towards "working well', we can further work on consistency— especially making sure every change comes with concrete tests and that our checks run automatically on every PR. Our next step is to treat tests as part of “done” for each LIC PR and keep `main` buildable and testable at all times.

## License

See [LICENSE](../LICENSE).
