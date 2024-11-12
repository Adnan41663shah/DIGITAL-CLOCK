![Screenshot 2024-11-12 191530](https://github.com/user-attachments/assets/74b455ba-facd-477c-8509-4b0feaa364cc)# DIGITAL-CLOCK
# Digital Clock by Adnan

A simple digital clock application built with Python and PyQt5. This clock displays the current time in `hh:mm:ss` format with a custom font and color scheme.

## Features

- Real-Time Clock: Displays the current time in `hh:mm:ss AP` format.
- Custom Font: Uses the `DS-DIGIT.TTF` font to give the clock a digital look. (The font will revert to Arial if not found.)
- Custom Styling: Green-colored text with a black background for a retro digital clock aesthetic.
- Automatic Updates: Updates every second to display the current time.

## Prerequisites

- Python 3.x
- PyQt5 (install via pip if not already installed)

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/Adnan41663shah/digital-clock.git
   cd digital-clock
   
Install PyQt5:
pip install PyQt5
Add the Font:

Ensure DS-DIGIT.TTF is in the project directory. You can download this font online if needed.
Usage

Run the digital_clock.py file to start the application:
python digital_clock.py


Code Overview
DigitalClock: A class that creates the main clock window, handles the font and layout setup, and updates the time every second.
initUI: Sets up the window title, size, font, colors, and layout.
update_time: Fetches the current time and updates the display every second.

screenshots:
![Screenshot 2024-11-12 191530](https://github.com/user-attachments/assets/98d90c31-305e-4b7d-a0fa-bb3649ff0226)
![Screenshot 2024-11-12 191517](https://github.com/user-attachments/assets/9c604ddd-ce75-478d-bda7-bcedbc655726)

License
This project is licensed under the MIT License.









