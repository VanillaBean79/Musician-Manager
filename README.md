# Musician Manager App

Musician Manager is a simple command-line application that allows you to manage musicians and their managers. The app uses SQLite to store data and provides basic CRUD (Create, Read, Update, Delete) functionality for managing both musicians and managers. The application allows users to:

- Create new musicians and managers
- View all musicians and managers
- Update musician and manager details
- Delete musicians and managers
- List musicians assigned to a specific manager

## Features

### Manager Management
- **Create**: Add a new manager to the system.
- **View**: List all managers or search for a manager by name.
- **Update**: Modify a manager's details.
- **Delete**: Remove a manager from the system.

### Musician Management
- **Create**: Add a new musician and assign a manager.
- **View**: List all musicians or search for a musician by name.
- **Update**: Modify a musician's details (name, age, instrument, category, and manager).
- **Delete**: Remove a musician from the system.
  
### Database
- The app uses SQLite as its database engine, and the data is stored in two tables: `managers` and `musicians`.
  
## Setup

### Requirements

- Python 3.x
- SQLite (comes with Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VanillaBean79/Musician-Manager.git
   cd Musician-Manager

2. python cli.py