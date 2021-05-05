# GIT Manager
# Adeeb

while True:
    init = input("Enter Command: ").lower()

    if init == 'exit'.lower():
        break
    elif init != 'git init'.lower():
        print("Git not initialized. Enter a valid command, or type 'exit' to exit the program")
        continue
    else:
        print("Initialized. Now you can use GIT Manager")

        serial_no = 0
        serial_numbers = []
        current = ''
        commits = {}

        while True:
            sentence = ""
            message = input("Enter Command: ")

            if len(message.split()) > 2:
                split_message = message.split()
                keyword_temp = split_message[0:2]
                keyword = ' '.join(map(str, keyword_temp))
                words = split_message[2:]
                sentence = ' '.join(map(str, words))
            else:
                keyword = message

            if keyword.lower() == 'git commit':
                if sentence[0] == '"' and sentence[-1] == '"':
                    serial_no += 1
                    serial_numbers.insert(0, serial_no)
                    current = serial_numbers[0]
                    sentence = sentence[1:-1]
                    commits[serial_no] = str(sentence)

                    print(f"Current Sequence Number : {current}")
                    print(f"All Commits: {commits}")
                else:
                    print("Wrong Message Format")

            elif keyword.lower() == 'git update':
                if sentence[0] == '"' and sentence[-1] == '"':
                    sentence = sentence[1:-1]
                    for key, value in list(commits.items()):
                        commits[current] = sentence

                    print(f"Current Sequence Number : {current}")
                    print(f"All Commits: {commits}")
                else:
                    print("Wrong Format")

            elif keyword.lower() == 'git delete':
                try:
                    for key, value in list(commits.items()):
                        if key == int(sentence):
                            del commits[key]
                            new_position = serial_numbers.index(current)
                            serial_numbers.remove(key)
                            if current == key:
                                if new_position < len(serial_numbers):
                                    current = serial_numbers[new_position]
                                else:
                                    current = serial_numbers[len(serial_numbers)-1]
                except ValueError:
                    print("Invalid Sequence Number!")
                except IndexError:
                    current = None
                    serial_no = 0
                    print("Sequence List is empty now!")

                print(f"Current Sequence Number : {current}")
                print(f"All Commits: {commits}")

            elif keyword.lower() == 'git jump':
                flag = 0
                try:
                    jump_id = int(sentence)
                    if jump_id in serial_numbers:
                        current = jump_id
                        flag = 1
                except ValueError:
                    print("Invalid Sequence Number!")

                if flag == 0:
                    print("Commit ID Not Found!")

                print(f"Current Sequence Number : {current}")
                print(f"All Commits: {commits}")

            elif keyword.lower() == 'git backward-commit':
                if serial_numbers.index(current) < len(serial_numbers)-1:
                    new_position = serial_numbers.index(current)+1
                    current = serial_numbers[new_position]
                else:
                    print("Cant go any more backward!!")

                print(f"Current Sequence Number : {current}")

            elif keyword.lower() == 'git forward-commit':
                if serial_numbers.index(current) > 0:
                    new_position = serial_numbers.index(current)-1
                    current = serial_numbers[new_position]
                else:
                    print("Cant go any more forward!")

                print(f"Current Sequence Number : {current}")

            elif keyword.lower() == 'git show' and sentence.lower() == 'commit':
                for key, value in list(commits.items()):
                    if key == int(current):
                        print(f"Current Commit Message: {value}")

            elif keyword.lower() == 'git show' and sentence.lower() == 'all commit':
                for position in serial_numbers:
                    for key, value in list(commits.items()):
                        if key == int(position):
                            print(f"{position} {value}")

            elif keyword.lower() == 'git pull':
                try:
                    to_pull = int(sentence)
                    if to_pull in serial_numbers:
                        serial_numbers.remove(to_pull)
                        serial_numbers.insert(0, to_pull)
                        current = serial_numbers[0]
                except ValueError:
                    print("Invalid Sequence Number!")

                print(f"Current Sequence Number : {current}")

            elif keyword.lower() == 'exit':
                break

            else:
                print("Unknown Command, Try again. or type 'exit' to terminate GIT Manager")
