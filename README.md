# Codesoft-Project-3

# Tic-Tac-Toe AI 🎮

A modern, visually stunning web-based implementation of the classic Tic-Tac-Toe game featuring an unbeatable AI opponent.

## 🌟 Features

- **Unbeatable AI:** The AI uses the Minimax algorithm enhanced with Alpha-Beta pruning to ensure it plays a perfect game every time. You can only draw or lose!
- **Modern UI:** Designed with a rich "Glassmorphism" aesthetic, featuring frosted glass panels, deep slate backgrounds, and vibrant neon accents.
- **Micro-animations:** Smooth transitions, hover effects, and satisfying "pop" animations when placing markers.
- **Player Selection:** Choose whether you want to play first as 'X' or second as 'O'. The AI instantly adapts.
- **Responsive Design:** Fully playable on both desktop and mobile screens.

## 🛠️ Technologies Used

- **HTML5:** For the structure of the game board and UI elements.
- **CSS3:** For styling, Flexbox/Grid layouts, custom properties (variables), and advanced animations (backdrop-filter for glassmorphism).
- **Vanilla JavaScript (ES6+):** For the core game logic, DOM manipulation, and AI algorithm implementation. No external frameworks or libraries are used.

## 🧠 How the AI Works

The game's AI is powered by the **Minimax Algorithm**, a decision rule used in artificial intelligence, decision theory, game theory, and statistics for minimizing the possible loss for a worst-case scenario.

To ensure the AI responds instantly, **Alpha-Beta Pruning** is applied on top of the Minimax algorithm. This optimization reduces the number of nodes evaluated by the algorithm in its search tree, completely skipping branches that won't yield a better result than previously evaluated moves.

## 🚀 How to Run

Since this is a vanilla frontend application, you do not need to install any dependencies or run a build step.

1. Clone or download this repository.
2. Navigate to the project folder.
3. Simply double-click the `index.html` file to open it in your default web browser.

## 🎮 How to Play

1. Open the game in your browser.
2. Select whether you want to play as **X (First)** or **O (Second)** using the toggle at the top.
3. Click on any empty cell on the 3x3 grid to place your marker.
4. Try to get 3 of your markers in a row (horizontally, vertically, or diagonally).
5. If the board fills up without a winner, the game is a Draw.
6. Click **Restart Game** to play again.

