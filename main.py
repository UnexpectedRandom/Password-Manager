from getpass import getpass

def addPassword():
    file = input('Choose A File To Add The Password In: ')
    subject = input('Whats The Subject: ')
    password = getpass('Whats The Password: ')
        
    try:
        with open(file, 'w') as passwordFile:
            passwordFile.write(subject+' - '+password)
    except Exception as e:
        print(f'[-] {e}')

try:
    while True:
        command = input("What would you like to do: ")
        
        if command == '-help' or command == '-h':
            print("""\n-q - Quit command line
-a - Add A New Password
-f - Add A New File
-n - same as -a
-help - help command\n""")
            
        if command == '-q':
            break

        if command == '-a':
            addPassword()
            
        if command == '-n':
            addPassword()
            
        if command == '-f':
            fileName = input('Whats The File Name: ')
            try:
                with open(fileName, 'x') as FL:
                    FL.close()
                print('[+] Created {fileName}')
            except Exception as e:
                print(f'[-] {e}')
except:
    print("\n[-] Error")
