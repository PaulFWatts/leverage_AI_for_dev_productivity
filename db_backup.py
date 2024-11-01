import logging
import shutil

# Configure logging
logging.basicConfig(
    filename="db_backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

active_db_file = "app.db"
backup_db_file = "backup.db"


def backup_db():
    try:
        shutil.copy(active_db_file, backup_db_file)
        logging.info("Backup successful")
    except Exception as e:
        logging.error("Backup failed: %s", e)


def restore_db():
    try:
        shutil.copy(backup_db_file, active_db_file)
        logging.info("Restore successful")
    except Exception as e:
        logging.error("Restore failed: %s", e)


def main():
    while True:
        print("1. Backup")
        print("2. Restore")
        print("3. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                backup_db()
                break
            case "2":
                restore_db()
                break
            case "3":
                logging.info("Exiting...")
                break
            case _:
                logging.warning("Invalid choice, please try again")


if __name__ == "__main__":
    main()
