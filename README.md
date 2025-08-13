# 🎮 Tic-Tac-Toe (Python Console Game)

A simple **console-based Tic-Tac-Toe** game built in Python. Play against another human player in the terminal.

---

## 📂 Project Structure
```
tic_tac_toe/
│
├── main.py            # Entry point for the game
├── game/              # Package containing all game logic
│   ├── __init__.py    # Marks this folder as a package
│   ├── board.py       # Handles board display
│   ├── game_logic.py  # Game rules and loop
│   └── utils.py       # Helper functions (player input)
└── README.md          # Project description and instructions
```

---

## 🚀 How to Run
### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/tic_tac_toe.git
cd tic_tac_toe
```

### 2️⃣ Run the game
```bash
python main.py
```

---

## 🕹 Gameplay Instructions
1. The board has positions numbered **1–9**.
2. Player **X** always starts.
3. Players take turns entering a number to mark their symbol.
4. The first to align **3 symbols** in a row, column, or diagonal wins.
5. If the board is full and no winner, the game ends in a **draw**.

---

## 🛠 Features
- ✅ Two-player mode
- ✅ Input validation
- ✅ Replay option
- ✅ Clear modular structure

---

## 📸 Example Output
```
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Enter your move X (1-9): 5
 X | 2 | 3
---|---|---
 4 | X | 6
---|---|---
 7 | 8 | 9
```
