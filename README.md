
### 🛡️ MySQL Backup & Recovery Utility

A Python-based utility to **backup**, **restore**, and **inspect** MySQL databases. Supports backup of individual tables, full databases, or all user databases, and includes intelligent recovery that avoids data duplication.

---

## 📦 Features

- ✅ Backup single table, full database, or all user databases.
- 📂 Saves backups in timestamped `.txt` files with metadata.
- 🔎 Parse backups to view table structure and content.
- ♻️ Restore deleted/missing data without duplicating existing rows.
- 🔧 Modular structure for easy maintenance.

---

## 🧩 Project Structure

```
mysql_backup_project/
├── main.py               # Main runner file with menu
├── backup_utils.py       # Functions for backing up MySQL data
├── recovery_utils.py     # Functions to parse & recover from backups
├── backups/              # Folder where backup files are stored
│   └── DB_Name/
│       ├── TableQueries_BackupTime.txt
│       └── ...
```

---

## ⚙️ How to Use

# 1. Set Your Configuration

Edit the variables in `main.py`:
```python
host = ""
user = ""
password = ""
db_name = ""
table_name = ""
backup_root = ""
```

# 2. Run the Script

```bash
python main.py
```

You'll be prompted with:
```
Select an operation:
1. Backup a specific table
2. Backup an entire database
3. Backup all user databases
4. Parse backup folder
5. Recover lost data from backup
```

Choose your operation and follow the instructions.

---

## 📁 Backup File Format

Each backup file includes:
```
-- Backup Timestamp: YYYY-MM-DD HH:MM:SS
-- Database Name: your_db
-- Table Name: your_table
-- Backed Up By: admin_user
-- MySQL Version: 8.x

--------------------------------------------------
QUERY TO CREATE TABLE IN THE DATABASE;

CREATE TABLE your_table (...);

--------------------------------------------------
QUERY TO INSERT THE RECORDS INTO THE TABLE;

INSERT INTO your_table VALUES (...);
```

---

## ♻️ Recovery Mode

Recovery automatically:
- Re-creates databases/tables if missing.
- Loads data into a temporary table.
- Only inserts records that don’t already exist.

---

## 🧪 Requirements

- Python 3.x
- MySQL server
- Python modules: `mysql-connector-python`

Install with:
```bash
pip install mysql-connector-python
```

---

## 👨‍💻 Author

**Yug Agarwal**

* 📧 Email – [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
* 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
* 💼 LinkedIn – [yugagarwal704](https://www.linkedin.com/in/yugagarwal704/)
* 🌐 Portfolio – [yugagarwal.dev](https://yugagarwal.dev/?utm_source=github&utm_medium=readme&utm_campaign=MySQL-Backup-Recovery-Utility_readme)