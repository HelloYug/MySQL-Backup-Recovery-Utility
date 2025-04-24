### File: main.py

from backup_utils import backup_table, backup_database, backup_all_databases
from recovery_utils import parse_backup_folder, recover_from_backups
import mysql.connector as msc
import os

# ----------------------------
# INPUTS (Set your values here)
# ----------------------------
host = "localhost"
user = "root"
password = "tiger"
db_name = "csproject"     # For OnlyTable / OnlyDatabase mode
table_name = "users"       # For OnlyTable mode
backup_root = "backups"

# Establish DB connection
mydb = msc.connect(host=host, user=user, password=password)
mycur = mydb.cursor()

# ----------------------------
# Menu for operation selection
# ----------------------------
print("Select an operation:")
print("1. Backup a specific table")
print("2. Backup an entire database")
print("3. Backup all user databases")
print("4. Parse backup folder")
print("5. Recover lost data from backup")

choice = input("Enter choice (1/2/3/4/5): ").strip()

if choice == "1":
    backup_table(mycur, db_name, table_name, user, backup_root)
    print(f"Table '{table_name}' from '{db_name}' backed up successfully.")

elif choice == "2":
    backup_database(mycur, db_name, user, backup_root)
    print(f"Database '{db_name}' backed up successfully.")

elif choice == "3":
    backup_all_databases(mycur, user, backup_root)
    print("All user databases backed up successfully.")

elif choice == "4":
    folder_path = os.path.join(backup_root, db_name)
    parse_backup_folder(folder_path)

elif choice == "5":
    folder_path = os.path.join(backup_root, db_name)
    recover_from_backups(folder_path, host, user, password)

else:
    print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

mydb.close()
