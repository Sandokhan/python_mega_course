user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add': 
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.title())
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number =- 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Hey, you entered a unkown command.")

print("Bye, Bye!")

