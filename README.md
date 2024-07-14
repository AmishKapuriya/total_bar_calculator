# Bar Calculator Application

## Overview
This Python script creates a graphical user interface (GUI) using `tkinter` to calculate the total number of bars required for a concrete column based on user inputs for length, width, cover, and spacing. The application will show the results directly in the window, displaying the total number of bars and the number of bars on each side.

## Features
- **GUI for Input**: Input fields for cover, spacing, length, and width.
- **Calculation**: Calculates the number of bars based on the input values.
- **Result Display**: Shows the calculated total number of bars and the distribution on each side.
- **Keyboard Navigation**: Allows navigation between input fields using the `Enter` key.

## Files
- `bar.py`: The main Python script containing the application code.

## Dependencies
- `tkinter`: The standard Python interface to the Tk GUI toolkit.

## Usage
To run the application, execute the `bar.py` script. If you want to create a standalone executable, you can use `pyinstaller` with the `--noconsole` option to hide the command prompt window.

### Example:
```sh
pyinstaller --noconsole --onefile bar.py
```
## Contributing
Feel free to fork this repository, make changes, and create a pull request. Ensure your code is well-documented and follows the existing coding style.

## License
I am providing code and resources in this repository to you under an open source license. Because this is my personal repository, the license you receive to my code and resources is from me
```sh
Copyright 2024 Amish Kapuriya
