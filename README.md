# Flash Card Application
This is a simple Flash Card application built with Python's Tkinter library and pandas. It helps users learn French vocabulary by showing flash cards with French words on one side and their English translations on the other.

## Features
Flash Card Display: Displays a flash card with a French word and allows you to flip it to see the English translation.
Next Card Button: Moves to the next flash card after a delay.
Known Words Tracking: Allows users to mark words as known, which will then be removed from the learning list.

## Prerequisites
Python 3.x
pandas library
Tkinter library
Installation
Clone this repository:

sh
Copy code
git clone https://github.com/your-username/flash-card-app.git
Install the required Python libraries:

sh
Copy code
pip install pandas
Download or create the required CSV files:

french_words.csv: Contains French words and their English translations.
words_to_learn.csv: Used to track words that need to be learned (generated automatically after running the program for the first time).
Download or create the required image files:

card_front.png: Image for the front of the flash card.
card_back.png: Image for the back of the flash card.
right.png: Image for the button to mark words as known.
wrong.png: Image for the button to indicate unknown words.
Usage

## Run the application:

sh
Copy code
python flash_card_app.py
Use the interface:

Right Button: Marks the current word as known and moves to the next card.
Wrong Button: Shows the current card again.

## Code Overview
Data Handling: The application reads words from a CSV file and saves progress in another CSV file.
UI Setup: Uses Tkinter to create the graphical interface with buttons and card display.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Tkinter for creating the GUI.
pandas for data manipulation.
