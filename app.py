import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter.simpledialog import askstring

class TkinterSQLiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Manager")
        
        # Prompt user for the database name
        self.db_name = askstring("Database Name", "Enter the database name:")
        if not self.db_name:
            messagebox.showerror("Error", "Database name cannot be empty. Exiting.")
            root.destroy()
            return

        # Connect to SQLite database (or create if not exists)
        self.connection = sqlite3.connect(f"{self.db_name}.db")
        self.cursor = self.connection.cursor()

        # Create a list to store table names
        self.table_names = self.fetch_table_names()

        # Create widgets
        self.table_buttons_frame = ttk.Frame(root)
        self.table_buttons_frame.pack(pady=10)

        self.result_frame = ttk.Frame(root)
        self.result_frame.pack(pady=10)

        # Create buttons for each table
        self.create_table_buttons()

        self.entry_query = tk.Entry(root, textvariable=tk.StringVar())
        self.entry_query.pack(padx=10, pady=5)

        self.text_result = tk.Text(root, height=10, width=50)
        self.text_result.pack(padx=10, pady=10)

        self.button_execute_query = tk.Button(root, text="Execute Query", command=self.execute_query)
        self.button_execute_query.pack(pady=10)

        # Call show_table_data for the first table
        if self.table_names:
            self.show_table_data(self.table_names[0])

    def execute_query(self):
        try:
            query = self.entry_query.get()
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.display_results(results)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error executing the query.\n{str(e)}")

    def display_results(self, results):
        self.text_result.delete(1.0, tk.END)  # Clear previous results
        for row in results:
            self.text_result.insert(tk.END, str(row) + '\n')

    def fetch_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_column_names(self, table_name):
        self.cursor.execute(f"PRAGMA table_info({table_name});")
        return [row[1] for row in self.cursor.fetchall()]

    def create_table_buttons(self):
        for table_name in self.table_names:
            button = ttk.Button(self.table_buttons_frame, text=table_name, command=lambda t=table_name: self.show_table_data(t))
            button.pack(side=tk.LEFT, padx=5)

    def show_table_data(self, table_name):
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Fetch data from the selected table
        self.cursor.execute(f"SELECT * FROM {table_name};")
        data = self.cursor.fetchall()

        # Fetch column names
        column_names = self.fetch_column_names(table_name)

        # Display data in a treeview with horizontal scrolling
        tree = ttk.Treeview(self.result_frame, columns=column_names, show="headings")
        for column in column_names:
            tree.heading(column, text=column)
            tree.column(column, width=100)  # Adjust the width as needed

        # Add horizontal scrollbar
        tree_scroll_x = ttk.Scrollbar(self.result_frame, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=tree_scroll_x.set)
        tree_scroll_x.pack(side="bottom", fill="x")

        for i, row in enumerate(data):
            tree.insert("", i, values=row)

        tree.pack()

        # Save the current table name for add and delete operations
        self.current_table = table_name


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterSQLiteApp(root)
    root.mainloop()
