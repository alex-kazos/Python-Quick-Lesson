# Week 2 - Control Flow

## Main Goal

Learn that programs are instructions plus decisions.

## Concepts

- **`if`, `elif`, `else`**: These let a program make decisions. `if` checks the first condition, `elif` checks another condition if needed, and `else` runs when none of the previous conditions were true.
- **Comparisons**: Comparisons ask questions like "are these equal?" or "is this bigger?" Examples include `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- **Booleans**: A boolean is either `True` or `False`. Conditions in Python usually produce boolean values.
- **`for` loops**: A `for` loop repeats code for each item in a sequence, such as each number in a range or each answer in a list.
- **`while` loops**: A `while` loop repeats code as long as a condition stays true. These are useful for menus, retries, and games that keep running until the user quits.
- **Lists**: A list stores multiple values in order. For example, guesses, quiz questions, and scores can all be stored in lists.
- **Basic validation**: Validation means checking user input before trusting it. For example, the game should handle `"banana"` instead of crashing when it expects a number.


## Build

Run:

```powershell
python week_02_control_flow/guess_the_number.py
```

## Homework

Add:

- easy, normal, and hard difficulty
- score system
- replay option
- maximum and minimum guess range shown to the player

## Git Habit

Practice the normal loop:

```powershell
git status
git add .
git commit -m "Add guess the number game"
git push
```

## Done Means

- The game has at least one decision and one loop.
- Bad input does not instantly destroy the session.
- They can explain `if` vs `while`.
