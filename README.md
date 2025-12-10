# Login System Simulation

A simple **Python login system** with registration, hashed passwords, and persistent storage.
## Features

- Multiple user accounts
- Passwords securely hashed with SHA-256
- Persistent storage using `users.json`
- Registration system with immediate login
- Login attempts limited to 3

## Technologies Used

- Python 3
- `getpass` module (for hidden password input)
- `hashlib` module (for password hashing)
- `json` module (for storing user data)

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/mil4sec/login-system.git
```

2. Navigate into the project folder:

```bash
cd login-system
```


3. Run the program:

```bash
py login.py
```

4. Follow the on-screen menu to Register or Login.

## Usage Example
```
=== Login System ===
1. Login
2. Register
Select an option (1 or 2): 2
Choose a username: felixnavidad
Choose a password: 
User 'felixnavidad' registered successfully! You can now log in.

Select an option (1 or 2): 1
Enter username: felixnavidad
Enter password: 
Login successful! Welcome, felixnavidad!
```
