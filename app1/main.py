user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add': 
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.title())
        case 'exit':
            break
        case _:
            print("Hey, you entered a unkown command.")

print("Bye, Bye!")

