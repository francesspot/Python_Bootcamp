[Polski](README.md) | **English**

# Python Bootcamp — 100 Days of Code (Day 16+)

Continuation of my work on the **100 Days of Code: The Complete Python Pro Bootcamp** course, from Day 16 onwards — the part of the course where every project is a standalone script instead of a JetBrains Academy template. Days 1–15 are in the [Python_Basics](https://github.com/francesspot/Python_Basics) repository.

The focus here is **object-oriented programming** and simple games built with the `turtle` module.

## Projects

| Folder | Day | What it is |
|--------|-----|------------|
| `day-16-start` | 16 | Introduction to OOP; **Coffee Machine** rewritten with classes (`CoffeeMaker`, `Menu`, `MoneyMachine`) |
| `day-17-start` | 17 | Writing your own classes; **Quiz Game** (`Question`, `QuizBrain`) |
| `day-18-start` | 18 | Turtle graphics; **Hirst Painting** — a dot painting with colours extracted from an image |
| `day-19-start` | 19 | Event listeners; Etch-a-Sketch and a **Turtle Race** with betting |
| `snake_game` | 20–21, 24 | **Snake** — with a scoreboard and a high score saved to `data.txt` |
| `pong_game` | 22 | **Pong** for two players |
| `turtle-crossing-start` | 23 | **Turtle Crossing** — a Frogger-like game with levels that speed up |
| `day-24-start` | 24 | Reading and writing files |
| `Mail Merge Project Start` | 24 | **Mail Merge** — generates a personalised invitation letter for each name on a list |

## Requirements

Python 3 with `tkinter` (needed by `turtle`; included in the standard Windows/macOS installers). Two projects need extra packages:

```bash
pip install prettytable colorgram.py
```

## Running

Each game imports its own modules, so run it from inside its folder:

```bash
cd snake_game
python main.py
```

The Mail Merge script is the exception — it uses paths relative to the repository root:

```bash
python "Mail Merge Project Start/main.py"
```
