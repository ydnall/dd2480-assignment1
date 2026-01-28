# Assignment 1 - Launch Interceptor Program

This folder contains the implementation of the DECIDE program and its tests.

## Requirements
- Python 3.10+

## Run program


## Run tests (venv)

```
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## Statement of contributions

- Sumeya Yasir Isse: Made the solutions and ran tests for LIC 3, 4, 5; implemented FUV.

- Yiqin Lin: Made the solutions and ran tests for LIC 9, 10, 11; wrote README/documentation.

- Emma Lindblom: Made the solutions and ran tests for LIC 6, 7, 8.

- Andy Li: Made the solutions and ran tests for LIC 12, 13, 14; implemented CMV, __init__.py, and the top-level decide integration.

- Martin Zivojinovic: Made the solutions and ran tests for LIC 0, 1, 2; implemented PUM.

## Way of working (Essence self-assessment)

- We structured the work using GitHub Issues and feature branches. Each Launch Interceptor Condition (LIC) was tracked as its own issue, and each member implemented their assigned LIC(s) on a separate branch linked to that issue. Changes were integrated through pull requests, which required other group members to review before merging into the main branch. 
This helped keep the main branch clean and ensured that each merge represented a small, traceable change (an atomic commit). With the discussions and review history preserved in its corresponding PR.

Right now, our way of working is “working well”: we delegate clear tasks from the start, and we integrate regularly through reviewed PRs. The main thing we can further work on is consistency—especially making sure every change comes with concrete tests and that our checks run automatically. Hence, making tests part of the definition of “done” for every LIC PR and ensure the main branch stays buildable and testable at all times.

## License
See `LICENSE`.
