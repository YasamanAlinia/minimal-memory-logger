# Minimal Memory Logger

A simple CLI Python project to log and view memories in JSON.

---
## Demo

### ![CLI Demo](./demo/demo.svg)

---

## Features

- Add memory
- List all memories
- Generate a simple memory report

### Technical Highlights

- Stores and displays memories in JSON format
- wWell-documented code with docstrings
- Unit testing for core functionalities

---

## Prerequisites

- Python 3.11+

---

## Usage

Run the project

```bash
python -m memory_journal.main
```

Run tests

```bash
python -m unittest discover
```

Example session

```bash
$ python -m memory_journal.main
1. Add memory
2. Show all
3. Generate report
4. Exit
Choose: 1
--Write your memory--
My first memory...
--memory made successfully!--
```

---

## Notes

- This project is built entirely with python.
- It focuses on:
  - Readable and maintainable code
- Suitable for:
  - Learning and working with JSONs files

---

## Future Plans

- Analyze memories with machine learning techniques
- Add unit tests for all remaining actions
- Include enhanced reporting and visualization
