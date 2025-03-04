Musician Manager CLI
The Musician Manager CLI is a simple command-line application that allows you to manage a list of musicians and their associated managers. The app allows you to create, view, update, and delete musicians and managers. It uses a SQLite database (musicians.db) to store the data.

Features
Manage Managers: Create, view, find by name, and delete managers.
Manage Musicians: Create, view all, view musicians by manager, find musicians by name, and delete musicians.
Data Storage: All data is stored in an SQLite database.
Database Structure: There are two tables: managers and musicians, where each musician is associated with a manager via manager_id.
Project Structure
The project consists of the following Python files:

manager.py: Contains functions for managing managers (add, delete, view, etc.).
musician.py: Contains functions for managing musicians (add, delete, view, etc.).
helpers.py: Contains helper functions to format manager and musician data for display.
cli.py: Main entry point for the command-line interface. Contains the logic for interacting with the user and calling functions from manager.py, musician.py, and helpers.py.
create_tables.py: Contains code to set up the SQLite database with managers and musicians tables.
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-name>
Install required dependencies: This project uses Python’s built-in sqlite3 module, so no additional dependencies are required. However, ensure you have Python 3 installed on your machine.

Set up the database: Run the following command to create the necessary tables in the SQLite database:

bash
Copy code
python create_tables.py
Run the CLI: To start using the application, run the following command:

bash
Copy code
python cli.py
Usage
Once the application is running, the CLI will present you with a menu of options. You can:

Manage Managers: Create, view, find, and delete managers.
Manage Musicians: Create musicians, view all musicians, view musicians by manager, find musicians by name, and delete musicians.
Example CLI Workflow
Manage Managers:

To create a new manager, select option 1 and input the manager's name and age.
To view all managers, select option 2.
To delete a manager, select option 4 and provide the manager's name.
Manage Musicians:

To create a new musician, select option 1, and input the musician's information, including the manager they are associated with.
To view all musicians, select option 2.
To view musicians by manager, select option 3 and provide the manager's ID.
To delete a musician, select option 5 and provide the musician's name.
Sample CLI Interaction:
bash
Copy code
=== Musician Manager CLI ===
1. Manage Managers
2. Manage Musicians
0. Exit
Choose an option: 1

=== Manage Managers ===
1. Create Manager
2. View All Managers
3. Find Manager by Name
4. Delete Manager
0. Back to Main Menu
Choose an option: 1
Enter manager's name: Phil
Enter manager's age: 30
Manager Phil added successfully.

=== Musician Manager CLI ===
1. Manage Managers
2. Manage Musicians
0. Exit
Choose an option: 2

=== Manage Musicians ===
1. Create Musician
2. View All Musicians
3. View Musicians by Manager
4. Find Musician by Name
5. Delete Musician
0. Back to Main Menu
Choose an option: 1
Enter the manager's ID for this musician: 1
Enter musician's name: Jill
Enter musician's age: 25
Enter musician's instrument: Guitar
Enter musician's category: Rock
Musician Jill added successfully under manager ID 1.
Database Structure
Managers Table
id: INTEGER (Primary Key, Auto-Increment)
name: TEXT (Manager's name)
age: INTEGER (Manager's age)
Musicians Table
id: INTEGER (Primary Key, Auto-Increment)
name: TEXT (Musician's name)
age: INTEGER (Musician's age)
instrument: TEXT (Musician's instrument)
category: TEXT (Musician's category)
manager_id: INTEGER (Foreign Key, references managers(id))
File Descriptions
manager.py
Contains functions for managing managers:

create_manager(name, age): Creates a new manager.
view_all_managers(): Returns all managers.
find_manager_by_name(name): Finds a manager by name.
delete_manager(name): Deletes a manager by name.
musician.py
Contains functions for managing musicians:

create_musician(name, age, instrument, category, manager_id): Creates a new musician.
view_all_musicians(): Returns all musicians.
view_musicians_by_manager(manager_id): Returns musicians associated with a specific manager.
find_musician_by_name(name): Finds musicians by name.
delete_musician(name): Deletes a musician by name.
helpers.py
Contains helper functions:

format_manager(manager): Formats a manager for display.
format_musician(musician): Formats a musician for display.
cli.py
Contains the main menu and logic for interacting with the user. It calls functions from manager.py, musician.py, and helpers.py to allow the user to perform operations in the app.

create_tables.py
Contains the SQL commands to create the managers and musicians tables in the SQLite database.

Contributing
Feel free to open issues or submit pull requests if you find bugs or want to suggest improvements.

License
This project is open source and available under the MIT License.