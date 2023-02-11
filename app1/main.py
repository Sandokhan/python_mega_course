user_prompt = "Enter a todo: "

def get_todos(filename):
    with open(f'./files/{filename}', 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(filename, todos_args):
    with open(f'./files/{filename}', 'w') as file:
        file.writelines(todos_args)
    return None

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()


    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = get_todos('todos.txt')
        
        todos.append(todo + '\n')

        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')
        
        new_todos = [item.strip('\n') for item in todos]
        
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item.title()}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:]) 
            number =- 1

            todos = get_todos('todos.txt')
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('todos.txt', todos)
        
        except ValueError:
            print("Your command is not valid.")
            continue
        
    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])
            
            todos = get_todos('todos.txt')
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('todos.txt', todos)
            
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        
        except IndexError:
            print('There is not item with that index.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an invalid command.")

print("Bye, Bye!")

