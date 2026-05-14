# Week 3 - Functions and Modules

## Main Goal

Learn how functions make code easier to understand, change, and debug.

## Concepts

- **Defining functions**: A function is a named block of code that performs a task. Defining a function lets you reuse that task instead of copying the same code everywhere.
- **Parameters**: Parameters are inputs a function needs to do its job. For example, `def greet(name):` means the function expects a `name`.
- **Return values**: A return value is the result a function gives back. Returning a value is different from printing it; returned values can be reused by other code.
- **Local variables**: A local variable exists inside a function. It helps the function do its work without accidentally changing the rest of the program.
- **One function, one job**: Good functions are focused. A function that adds an expense should not also print the whole menu, save files, and calculate totals.
- **`if __name__ == "__main__"`**: This pattern tells Python which code should run when the file is executed directly. It also makes the file safer to import from another file later.

## Build

Run:

```powershell
python week_03_functions_and_modules/expense_tracker.py
```

## Homework

Add:

- food, transport, gaming, subscriptions categories
- category totals
- input validation for negative amounts
- option to remove an expense
- a clearer menu

## Git Habit

Use commit messages that describe the feature:

```text
Add category totals to expense tracker
```

## Done Means

- The app uses at least four functions.
- They can explain parameter and return value.
- The commit message says what changed.
