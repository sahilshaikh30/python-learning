# Python Learning

My practice scripts from learning Python, organized by topic. These are small programs written to understand one idea at a time: input handling, conditionals, loops, and object-oriented programming. Larger projects live in their own repos.

## Folders

### 01-basics-and-input
| File | What it does | Concepts practiced |
|---|---|---|
| `gradelens.py` | Takes marks for three subjects, then prints total, percentage, pass/fail result, and grade | `input()`, arithmetic, `if / elif / else` |
| `focusfit.py` | Scores your readiness for a focus session from sleep, energy, and available time | Conditionals, weighted scoring, f-strings |

### 02-loops-and-games
| File | What it does | Concepts practiced |
|---|---|---|
| `guess_num.py` | Number guessing game with higher/lower hints | `while` loops, `random`, counters |
| `snake_gun_water_game.py` | Snake-Water-Gun against the computer, with replay | Dictionaries, `random`, nested conditions |

### 03-oop
| File | What it does | Concepts practiced |
|---|---|---|
| `student_result_analyzer.py` | Student class that calculates total, average, and pass status | Classes, methods, class variables |
| `bank_acc_manager.py` | Bank account with deposit, withdraw, and balance report | Classes, methods, state changes |
| `employee_sal_manager.py` | Employee class that calculates total salary and high-earner status | Classes, methods, boolean returns |

`gradelens.py` and `student_result_analyzer.py` solve a similar problem, one with plain scripting and one with classes, so I could compare both approaches.

## Bigger projects
- [event-ticket-booking-system](https://github.com/sahilshaikh30/event-ticket-booking-system)
- [quiz-engine](https://github.com/sahilshaikh30/quiz-engine)
- [spendsense](https://github.com/sahilshaikh30/spendsense)

## How to run
Each file runs on its own with Python 3, with no installs needed:
```
python filename.py
```

## Known issues
These are learning scripts, so some skip input validation and can crash on unexpected input (for example, typing text where a number is expected). I'm noting them here and improving them over time.

## Next up
- SQL with Python (SQLite)
- Data analysis with pandas
- Basic machine learning
