import os
import shutil
import sys

def menu():
    while True:
        print("Enter operation\n");
        print("=====================");
        print("1:List directory\n");
        print("2:Enter directory\n");
        print("3:Return to previous directory\n");
        print("4:Create directory\n");
        print("5:delete directory\n");
        print("6:copy directory\n");
        print("7:move directory\n");
        print("8:quit\n");
        try:
            inp = int(input("--> "))

            if inp == 1:
                print(os.listdir())

            elif inp == 2:
                print("Enter directory name\n")
                inp = input()
                if os.path.isdir(inp):
                    os.chdir(inp)
                    print(f"Changed directory to {inp}")
                else:
                    print("Directory not found")

            elif inp == 3:
                os.chdir("..")

            elif inp == 4:
                inp = input("Directory name:\n")
                os.makedirs(inp, exist_ok=True)
                print("Directory created")

            elif inp == 5:
                inp = input("Directory name:\n")
                if os.path.isdir(inp):
                    c = input("You really want to delete? enter y/n\n ").lower()
                    if c == "y":
                        shutil.rmtree(inp)
                        print("Directory deleted\n")
                    else:
                        print("Cancelled\n")
                else:
                    print("Directory does not exist\n")
            elif inp==6:
                source=input("Enter path of directory to be copied:\n")
                destination=input("Enter path of new directory:\n")
                if os.path.exists(source):
                    print("Note: If the same directory exists, it will be overwritten.")
                    shutil.copytree(source,destination,dirs_exist_ok=True)
                    print("Directory copied")
                else:
                    print("Souce file doesnt exists")
            elif inp==7:
                source = input("Enter path of directory to be moved\n")
                destination = input("Enter path of new directory \n")
                if os.path.exists(source):
                    shutil.move(source, destination)
                    print("Directory moved\n")
                else:
                    print("Source directory doesnt exist\n")
            elif inp==8:
                print("Good bye user !!")
                sys.exit(1)
            else:
                print("Invalid input !!!!!")
                sys.exit(-1)
        except ValueError:
            print("Invalid input! Please enter a number.\n")
        except FileNotFoundError:
            print("Directory not found!\n")
        except PermissionError:
            print("Permission denied! Cannot modify this directory.\n")
        except Exception as e:
            print(f"An error occurred: {e}")



menu()