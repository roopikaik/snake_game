🐍 Snake Game in Python (Enhanced Version)

An enhanced version of the classic Snake Game developed using Python and Pygame, featuring background graphics, obstacles, and time-based reward food that increases the snake’s length significantly if eaten within a limited time.

This project was built and executed using PyCharm and is suitable for learning, teaching, and mini-project evaluation.

📌 Features

Classic Snake movement using arrow keys

Background image support

Snake head with directional eyes

Static obstacles (collision causes game over)

Normal food (increases length by 1)

Timed reward food (power-up):

Appears at a fixed location

Stays for a short duration

Changes position if not eaten in time

If eaten in time, snake grows by multiple blocks

Score tracking

Game Over and Restart options

🛠️ Technologies Used

Python 3.x

Pygame library

PyCharm IDE

📂 Project Structure
snake-game/
│── snake_game.py
│── background.png
│── README.md

▶️ How to Run the Game
1. Install Python

Ensure Python 3 is installed:

python --version


Download from:
https://www.python.org/downloads/

2. Install Pygame
pip install pygame

3. Run the Game

Navigate to the project directory and execute:

python snake_game.py


A game window will open.

🎮 Controls
Key	Action
⬅️ Left Arrow	Move Left
➡️ Right Arrow	Move Right
⬆️ Up Arrow	Move Up
⬇️ Down Arrow	Move Down
C	Restart after Game Over
Q	Quit Game
⭐ Reward Food Mechanism

Reward food appears for a limited time

If eaten within the time window:

Snake grows by multiple blocks

Bonus score is added

If not eaten:

Reward food changes position

This feature demonstrates:

Timers

Game state management

Power-up mechanics

🚧 Obstacles

Fixed obstacles are placed on the screen

Collision with obstacles results in Game Over

Helps increase game difficulty

📚 Learning Outcomes

This project helps understand:

Game loop architecture

Event handling

Collision detection

Timers and power-ups

Python lists and logic

Pygame rendering

🚀 Future Enhancements

Multiple levels with increasing difficulty

Sound effects and animations

High-score system

Object-oriented refactoring

Mobile-style smooth movement


📜 License

This project is open-source and free to use for educational purposes.
