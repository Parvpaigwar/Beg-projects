# My-projects
Games - 
1. # Aim Trainer

Aim Trainer is a Python-based game developed using Pygame to help users enhance their mouse aiming skills. The game features dynamically resizing targets and provides real-time updates on metrics like speed, accuracy, and total hits. Players must hit as many targets as possible before running out of lives, with each miss costing a life. This project is ideal for those looking to improve their mouse dexterity and timing through a fun and interactive medium.

2 . Turtle racimg game
Turtle Racing Game is an engaging Python-based simulation where players can watch colorful turtles race to the finish line. Developed using the turtle and random libraries, the game allows 2 to 10 racers to compete, each represented by a different color. Users can input the number of racers, and the game dynamically adjusts the starting positions and races the turtles across the screen. The first turtle to reach the top of the window wins, and its color is announced as the winner. This simple and interactive game is perfect for anyone interested in a fun, graphical representation of random movement and basic gaming logic.

3. Rock , paper and scissor
Rock, Paper, Scissors Game is a classic, interactive command-line game implemented in Python. Upon launching the game, players are greeted with the option to play or not. If the player chooses to play, they will face off against the computer in a simple yet engaging game of Rock, Paper, Scissors. Players make their choice by entering a number corresponding to Rock (1), Paper (2), or Scissors (3). The computer randomly selects its move, and the game announces the outcome of each round—whether the player won, lost, or tied. The game continues until the player chooses to quit by entering 'q'. Finally, the game displays the player's score, reflecting the number of times they have won against the computer.

4. Dice rolling game(PIG)
Dice Rolling Game is a simple and engaging Python game for 2 to 4 players. Each player takes turns rolling a virtual dice to accumulate points towards a target score of 50. Players can choose to roll the dice or pass their turn. However, rolling a '1' resets their total score to zero for that round, adding a layer of risk to each decision. The game continues until all players have either reached the target score or passed their turn. The player with the highest score wins, unless all players end up with zero points, resulting in a draw. This game combines chance with strategic decision-making, making it a fun and interactive experience for multiple players.

5. slot machine
The Python script you're working with simulates a slot machine game, allowing players to deposit funds, choose the number of lines to bet on, and place bets accordingly. It generates slot spins using a predefined set of symbols, calculates winnings based on the alignment of symbols across selected lines, and updates the player's balance after each spin. Players can continue to play by making new bets or quit the game by checking their balance. The game provides a straightforward yet engaging experience by combining random outcomes with strategic betting decisions.


OTHER PROJECTS -
1. youtbe downloader

This Python script creates a simple YouTube video downloader GUI application using the pytube library and tkinter for the graphical interface. Upon execution, the user can input a YouTube video URL, select a folder to save the downloaded video, and initiate the download process by clicking the "Get video!" button.

The DownloaderApp class sets up the main GUI window with a title, an entry field for the YouTube video URL, and a button to start the download process. The open_file_dialog function opens a file dialog to select the destination folder for saving the downloaded video.

The download_video function is responsible for downloading the video from the provided URL to the specified directory. It uses pytube to fetch the video streams, selects the highest resolution progressive stream in MP4 format, and downloads the video file to the specified directory. Upon completion or failure, it displays a corresponding message box.

The script utilizes threading to ensure that the GUI remains responsive during the download process. When the user initiates the download, the GUI button is disabled, and the download process runs in a separate thread, allowing the user to continue interacting with the application.

Overall, this script provides a user-friendly way to download YouTube videos with a simple and intuitive graphical interface.

2. Password generator
This Python script is a customizable password generator that allows users to specify the minimum length of the password and optionally include numbers and special characters. The function generate_password constructs the password by randomly selecting characters from a pool that includes letters, and conditionally, digits and punctuation based on user preferences. It ensures the password meets the user-specified criteria regarding length and character types before returning it. The script interacts with the user through prompts to determine these preferences, then generates and displays the resulting password.

3. WPM_typing test
This Python script implements a Speed Typing Test using the curses library, allowing users to practice typing by reproducing a randomly selected text as quickly as possible. The start_screen function displays a welcome message and prompts the user to begin the test by pressing any key. The display_text function updates the screen to show the target text, the user's current input, and their words per minute (WPM) score.

The load_text function reads a text file containing various passages, selects one at random, and returns it. The wpm_test function manages the typing test, continuously updating the screen with the target text, the user's input, and their calculated WPM score. Users can input characters to match the target text, and once the entire text is correctly typed, the test ends, and the user's completion time and WPM are displayed.

The main function initializes the curses environment, sets up color pairs, displays the start screen, and orchestrates the typing test loop. After completing each test, users can choose to continue or exit the program. Overall, this script provides an interactive and engaging way for users to improve their typing speed and accuracy.

4. dirking waterremainder (adjustable)
This Python script utilizes the plyer library to display periodic notifications reminding the user to take a break and drink water. Inside a continuous loop, it repeatedly sends notifications with a title, message, and a timeout of 5 seconds, prompting the user to take a break. The time.sleep(10) function call ensures that notifications are sent every 10 seconds. This script serves as a helpful tool for promoting healthy habits by encouraging regular breaks and hydration during extended computer usage sessions.

5. PDF_password cracker
This Python script attempts to crack the password of a PDF file using a brute force method. It reads passwords from a wordlist file (wordlist.txt) and iterates through each password, attempting to open the PDF file (remote.pdf) with the pikepdf library. If the password is correct, it prints a success message in green color indicating the found password and terminates the loop. If the password is incorrect, it prints a message in red color indicating the password being tried and continues to the next password in the wordlist. This script provides a simple way to automate the password cracking process for PDF files using a predefined list of passwords.

6. Automated File Backup

This Python script automates the daily backup of a folder (Screenshots in this case) to a destination directory (Backups) on the desktop. It uses the schedule library to schedule the backup operation to occur daily at a specified time (18:57 in this example).
The copy_folder_to_directory function copies the contents of the source directory to a new directory named after the current date within the destination directory. If a folder with the same name already exists in the destination, it prints a message indicating that the folder already exists.
The script continuously checks for pending scheduled tasks using a while True loop. Upon reaching the scheduled time, it executes the backup operation and then waits for the next scheduled time. This script provides a convenient way to automate routine backup tasks, ensuring data integrity and security.
