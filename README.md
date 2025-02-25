Musician and Manager CLI Application
Overview
This command-line interface (CLI) application helps to manage musicians and managers using an SQLite database. The user can create, view, find, and delete musicians and managers, and link musicians to managers. The application is built in Python, utilizing SQLite for storing data persistently.

Project Structure
plaintext
Copy
.
├── manager.py
└── musicians.db
manager.py (CLI Script)
The manager.py file is the core of the project. It provides the CLI through which the user can interact with the application, execute commands, and manage the data. This script includes functions for creating and deleting managers and musicians, viewing the records, and searching for data in the SQLite database.

CLI Functions
create_manager(name, age)

Inserts a new manager record into the managers table with the given name and age.
create_musician(name, age, instrument, category, manager_id)

Inserts a new musician record into the musicians table. The musician is associated with a manager by the manager_id.
view_all_managers()

Displays all managers stored in the managers table.
view_all_musicians()

Displays all musicians stored in the musicians table.
find_manager_by_name(name)

Finds and displays a manager's details based on the provided name.
find_musician_by_name(name)

Finds and displays musicians whose names match the provided input. It performs a partial search, allowing the user to input only a portion of the name.
view_musicians_by_manager(manager_id)

Lists all musicians associated with a specific manager, using the manager_id.
delete_manager(name)

Deletes a manager from the database by their name.
delete_musician(name)

Deletes a musician from the database by their name.
cli()

The main CLI loop where the user is presented with a menu of options. The user selects an action (such as creating a manager, creating a musician, viewing data, etc.) and the corresponding function is called to execute the action.
Example of usage in the CLI:

bash
Copy
=== Musician Manager CLI ===
1. Create Manager
2. Create Musician
3. View All Managers
4. View All Musicians
5. View Musicians by Manager
6. Find Manager by Name
7. Find Musician by Name
8. Delete Manager
9. Delete Musician
0. Exit
Choose an option: 1
Enter manager's name: John Doe
Enter manager's age: 45
musicians.db (Database File)
This is the SQLite database where all data (managers and musicians) are stored. It contains two tables:

managers Table:

id: Unique identifier for the manager.
name: The manager's name.
age: The manager's age.
musicians Table:

id: Unique identifier for the musician.
name: The musician's name.
age: The musician's age.
instrument: The instrument the musician plays.
category: The musical category or section the musician belongs to (e.g., strings, percussion).
manager_id: Foreign key referencing the id of the manager who manages the musician.
Detailed Description of Functions
Manager Functions
create_manager(name, age)

Inserts a manager into the managers table.
Arguments:
name: A string representing the manager's name.
age: An integer representing the manager's age.
delete_manager(name)

Deletes a manager by their name.
Arguments:
name: A string representing the manager's name to be deleted.
find_manager_by_name(name)

Fetches a manager’s details based on the input name.
Arguments:
name: A string representing the manager's name.
view_all_managers()

Retrieves and displays all managers in the managers table.
Musician Functions
create_musician(name, age, instrument, category, manager_id)

Adds a musician to the musicians table.
Arguments:
name: A string representing the musician’s name.
age: An integer representing the musician’s age.
instrument: A string representing the instrument the musician plays.
category: A string representing the category the musician falls under (e.g., strings, percussion).
manager_id: The ID of the manager associated with the musician.
delete_musician(name)

Deletes a musician by their name.
Arguments:
name: A string representing the musician's name to be deleted.
find_musician_by_name(name)

Searches and retrieves musicians whose names match the input string.
Arguments:
name: A string representing the musician’s name or part of the name for a partial match.
view_musicians_by_manager(manager_id)

Displays all musicians that are managed by a specific manager, identified by the manager_id.
Arguments:
manager_id: An integer representing the ID of the manager.
view_all_musicians()

Displays all musicians from the musicians table.
Setting Up and Running the Application
Clone the repository to your local machine:

bash
Copy
git clone https://github.com/yourusername/musician-manager-cli.git
Change into the project directory:

bash
Copy
cd musician-manager-cli
Set up a virtual environment (optional but recommended):

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Run the application:

bash
Copy
python manager.py
