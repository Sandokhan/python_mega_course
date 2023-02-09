user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add': 
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}. {item.title()}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number =- 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
             number = int(input("Number of the todo to complete: "))
             todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Hey, you entered a unkown command.")

print("Bye, Bye!")

