# PC Power Control

A simple Python command-line utility to shut down, restart, or put a computer to sleep after a specified countdown.

## Why I Built This

One night, I fell asleep at the beginning of a movie and woke up to find my laptop battery completely drained. I decided to build a program that would automatically shut down my computer after the movie finished.

## Features

- Shut down, restart, or suspend the computer.
- Set a custom countdown in seconds.
- Validate user input.
- Cancel the countdown using `Ctrl+C`.
- Support for Windows and Linux.

## Requirements

- Python 3
- Windows or Linux

No external packages required.

## How to Run

Run the following command from your terminal:

```bash
python3 cd-timer.py
```

On Windows, you can also use:

```bash
python cd-timer.py
```

Choose an action, enter the countdown duration in seconds, and let the program handle the rest.

## Important Notes

- Save your work before running a shutdown or restart.
- The selected action executes automatically when the countdown finishes.
- System permissions and configuration may affect whether an action succeeds.

## What I Practised

This project helped me practise Python loops, conditional statements, input validation, exception handling, modules, and basic operating-system interaction.
