1. Import necessary libraries: The code starts by importing the required libraries, including `pygame`, `sys`, and `random`.

2. Initialize Pygame: The Pygame library is initialized using `pygame.init()`.

3. Define game constants and colors: Several constants such as window dimensions, gravity, bird jump velocity, pipe gap, and pipe velocity are defined. Additionally, color constants for white, black, and the bird color (yellow) are defined.

4. Create the game window: The Pygame window is created using `pygame.display.set_mode()` with the specified width and height. The window caption is set to "Flappy Bird" using `pygame.display.set_caption()`.

5. Set up font: A font for displaying text is set up using `pygame.font.SysFont()`.

6. Define the Bird class: The `Bird` class is defined to represent the flappy bird in the game. It has attributes for the bird's position, velocity, and gravity. The class also has methods for jumping, updating the bird's position, and drawing the bird on the screen.

7. Define the Pipe class: The `Pipe` class is defined to represent the pipes that the bird needs to navigate through. It has attributes for the pipe's position, height, and whether it has been passed by the bird. The class also has methods for updating the pipe's position and drawing the pipe on the screen.

8. Define utility functions:
   - `check_collision(bird, pipes)`: This function checks for collisions between the bird and the pipes. It returns `True` if there is a collision, and `False` otherwise.
   - `display_score()`: This function displays the current score and the high score on the screen.

9. Define the `main()` function: This is the main game loop. It sets up the game elements, initializes the bird and pipes, and enters the game loop.

10. `show_start_screen()`: This function displays the start screen with the text "Press SPACE to Start" and waits for the player to press the space key to start the game.

11. Main game loop:
    a. The `current_score` and `high_score` are initialized to 0.
    b. The bird and pipes are created and set up.
    c. The game loop starts with two nested while loops:
        - The outer loop (`while True`) handles restarting the game when the bird collides with a pipe.
        - The inner loop (`while True`) runs the game as long as the player is playing.
    d. In the inner loop, events are checked for user input, such as quitting the game or making the bird jump when the space key is pressed.
    e. The screen is filled with black to clear previous drawings.
    f. The bird and pipes are updated and drawn on the screen.
    g. Scoring is checked, and if the bird passes a pipe, the score is increased.
    h. Collision detection is performed to check if the bird collides with the pipes or goes out of the screen boundaries.
    i. If there is a collision, the inner loop breaks, and the player is taken back to the start screen to play again.

12. Start the game: Finally, the `main()` function is called to start the game.
