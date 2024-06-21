# Typing Speed Test

Typing Speed Test is a desktop application built using Python and Tkinter. It allows users to test their typing speed by typing a randomly selected sentence within a specified time frame.

## Features

- Randomly selects a sentence from a list of 30 sentences.
- Displays a countdown timer before the test begins.
- Calculates and displays the typing speed in words per minute (WPM).
- Notifies the user if the typed text does not match the sample text.
- Provides a reset button to restart the test with a new sentence.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Black-Scorpio/typing-speed-test
    ```

2. Navigate to the project directory:
    ```bash
    cd typing-speed-test
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. The application window will open. Follow these steps:
    - Click the **Start** button to begin the countdown.
    - Once the countdown reaches zero, start typing the sentence displayed.
    - Press **Enter** to submit your text.
    - The typing speed will be displayed if the typed text matches the sample text.
    - Click the **Reset** button to restart the test with a new sentence.

## Project Structure

```plaintext
typing-speed-test/
│
├── data.py               # Contains the list of sentences and function to get a random sentence
├── logic.py              # Contains the logic for starting, ending the test, and calculating typing speed
├── ui.py                 # Contains the UI components and layout using Tkinter
├── main.py               # Entry point for the application
└── README.md             # Project documentation
