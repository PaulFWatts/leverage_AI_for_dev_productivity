import shutil

active_db_file = 'app.db'
backup_db_file = 'backup.db'

def backup_db():
    try:
        shutil.copy(active_db_file, backup_db_file)
        print('Backup successful')
    except Exception as e:
        print('Backup failed:', e)

def restore_db():
    try:
        shutil.copy(backup_db_file, active_db_file)
        print('Restore successful')
    except Exception as e:
        print('Restore failed:', e)
        
def main():
    while True:
        print('1. Backup')
        print('2. Restore')
        print('3. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                backup_db()
                break
            case '2':
                restore_db()
                break
            case '3':
                print('Exiting...')
                break
            case _:
                print('Invalid choice, please try again')

if __name__ == '__main__':
    main()

    
