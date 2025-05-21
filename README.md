# 📝 To-Do List (Terminal App)

A simple, menu-driven command-line To-Do List program written in Python. Tasks are saved to a local text file (`todo.txt`) so they persist between sessions.

---

## 📂 Features

- ✅ Add new tasks
- 📋 View all current tasks
- 🗑️ Delete a specific task
- 🔥 Delete all tasks
- ✏️ Edit any existing task
- 💾 Automatic save to `todo.txt`

---

## 🚀 How to Run

### 1. Make sure you have Python installed.

### 2. Run the script:

```bash
python todo.py
```

---

## 📋 Menu Options

When running, you’ll see:

```
--- TO-DO LIST --- 
 1. Add Task 
 2. Show Tasks 
 3. Delete Task 
 4. Delete All 
 5. Edit Task 
 6. Exit
```

Follow the prompts by entering the number of the desired action.

---

## 📁 File Structure

```
todo.py       # The main Python program
todo.txt      # Stores your tasks (auto-generated if it doesn't exist)
README.md     # This file
```

---

## 💡 Example Usage

```
--- TO-DO LIST --- 
1. Add Task 
2. Show Tasks 
3. Delete Task 
4. Delete All 
5. Edit Task 
6. Exit
Press the number of your desired action: 1
Type your task: Finish homework
Task Added.
```

---

## 🧱 How It Works

- On start, it checks for an existing `todo.txt` and loads your saved tasks.
- Each action updates the file instantly, so your list is always current.
- Task numbers shown to the user are **1-based** (but handled with 0-based indexing internally).

---

## 🛠️ Improvements To Consider

- Input validation (non-integer inputs)
- Mark tasks as completed
- Add timestamps or priority
- Add color to output (via `colorama` or ANSI codes)
- Export to CSV or JSON

---

## ✅ Requirements

- Python 3.x
- No external libraries needed

---

## 📄 License

This project is free to use, modify, and share.
