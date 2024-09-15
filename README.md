# Python Snake Game

This is a classic Snake game implemented in Python using the Pygame library. The game features a snake that grows longer as it eats food, with the objective of achieving the highest possible score without colliding with the walls or the snake's own body.

## Features

- Smooth snake movement
- Random food generation
- Score tracking
- Game over screen with replay option

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-snake-game.git
   ```
2. Navigate to the project directory:
   ```
   cd python-snake-game
   ```
3. Install the required packages:
   ```
   pip install pygame
   ```

## How to Play

Run the game by executing the following command in the terminal:

```
python snake_game.py
```

- Use the arrow keys to control the snake's direction.
- Eat the food to grow longer and increase your score.
- Avoid colliding with the walls or the snake's own body.
- Press 'Q' to quit or 'C' to play again when the game is over.

## Project Structure

- `snake_game.py`: Main game loop and initialization
- `game_settings.py`: Game constants and settings
- `snake.py`: Snake class definition
- `food.py`: Food class definition
- `scoreboard.py`: Scoreboard class definition

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes. You can also open issues for any bugs you find or features you'd like to suggest.

## License

This project is open source and available under the [MIT License](LICENSE).
