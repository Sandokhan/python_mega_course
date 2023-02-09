user_prompt = "Enter a todo: "

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case 'add': 
            todo = input(user_prompt) + '\n'

            with open('./files/todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('./files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('./files/todos.txt', 'r') as file:
                todos = file.readlines()
            
            new_todos = [item.strip('\n') for item in todos]
            
            for index, item in enumerate(new_todos):
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

