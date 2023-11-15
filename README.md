# SQLite Tkinter App - Developer's README

## Overview
This README is intended for developers contributing to or working with the SQLite Tkinter App code. The application is a Python-based GUI tool that utilizes Tkinter and SQLite to interact with a database. It allows users to execute SQL queries, view table data, and perform basic operations like adding and deleting records.

## Table of Contents
1. [File Structure](#file-structure)
2. [Key Functions](#key-functions)
    - [TkinterSQLiteApp.__init__](#tkintersqliteappinit)
    - [TkinterSQLiteApp.execute_query](#tkintersqliteappexecute_query)
    - [TkinterSQLiteApp.display_results](#tkintersqliteappdisplay_results)
    - [TkinterSQLiteApp.fetch_table_names](#tkintersqliteappfetch_table_names)
    - [TkinterSQLiteApp.fetch_column_names](#tkintersqliteappfetch_column_names)
    - [TkinterSQLiteApp.create_table_buttons](#tkintersqliteappcreate_table_buttons)
    - [TkinterSQLiteApp.show_table_data](#tkintersqliteappshow_table_data)

## File Structure
- `app.py`: Main script containing the TkinterSQLiteApp class and the application's entry point.
- `LICENSE`: MIT License file.
- `README.md`: Project documentation.
- `songs.db`: Sample database.

## Key Functions

### TkinterSQLiteApp.__init__
- **Description:** Initializes the TkinterSQLiteApp class.
- **Parameters:**
  - `root`: The Tkinter root window.
- **Functionality:**
  - Prompts the user for the database name.
  - Connects to the SQLite database or creates a new one.
  - Creates the main GUI components (buttons, entry, text area).

### TkinterSQLiteApp.execute_query
- **Description:** Executes an SQL query entered by the user.
- **Functionality:**
  - Gets the SQL query from the entry widget.
  - Executes the query using the SQLite cursor.
  - Displays the results in the text area.

### TkinterSQLiteApp.display_results
- **Description:** Displays query results in the text area.
- **Parameters:**
  - `results`: List of rows resulting from an SQL query.
- **Functionality:**
  - Clears the previous results in the text area.
  - Inserts each row of results into the text area.

### TkinterSQLiteApp.fetch_table_names
- **Description:** Fetches the names of tables in the database.
- **Returns:**
  - List of table names.

### TkinterSQLiteApp.fetch_column_names
- **Description:** Fetches the names of columns in a given table.
- **Parameters:**
  - `table_name`: Name of the table.
- **Returns:**
  - List of column names.

### TkinterSQLiteApp.create_table_buttons
- **Description:** Creates buttons for each table in the GUI.
- **Functionality:**
  - Gets the list of table names.
  - Creates a button for each table, linked to `show_table_data` method.

### TkinterSQLiteApp.show_table_data
- **Description:** Displays the data of a selected table in a Treeview.
- **Parameters:**
  - `table_name`: Name of the selected table.
- **Functionality:**
  - Clears previous results in the result frame.
  - Fetches and displays data from the selected table in a Treeview widget.


## Contributing
If you want to contribute to this project, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License
This project is licensed under the [MIT License](LICENSE).
