const init = () => {
const todoBox = document.querySelector('#todo_box');
const todoInput = document.querySelector('#add_todo_input');
const todoBtn = document.querySelector('#add_todo_btn');
const reverseBtn = document.querySelector('#reverse_btn');
const dummyBtn = document.querySelector('#fetch_btn');
const clearBtn = document.querySelector('#clear_btn');

const fetchData = URL => {
    fetch(URL)
        .then(res => res.json())
        .then(todos => {
            for (const todo of todos) {
                todoBox.appendChild(createTodo(todo.title, todo.completed));
            }
        })
};

const createTodo = (inputText, completed = false) => {
    // Card
    const todoCard = document.createElement('div');
// if (completed) {
//     todoCard.className = 'ui secondary segment todo-item';
// } else {
//     todoCard.className = 'ui segment todo-item'
// }
// todoCard.className = 'ui segment todo-item';

    todoCard.classList.add('ui', 'segment', 'todo-item');
    if (completed) {
        todoCard.classList.add('secondary');
    }
    // Card > Wrrapper
    const wrapper = document.createElement('div');
    wrapper.classList.add('ui', 'checkbox');
    // Card > Wrrapper > input(checkbox)
    const input = document.createElement('input');
    input.setAttribute('type', 'checkbox');
    input.checked = completed;

    input.addEventListener('click', e => {
        if (completed) {
            label.classList.remove('completed-label');
            todoCard.classList.remove('secondary');
        } else {
            label.classList.add('completed-label');
            todoCard.classList.add('secondary');
        }
        completed = !completed;
        // input.checked = completed;
    });

    // Card > Wrrapper > input(text)
    const label = document.createElement('label');
    label.innerHTML = inputText;
    if (completed) {
        label.classList.add('completed-label');
    }
    // Card > Icon(delete)
    const deleteIcon = document.createElement('i');
    deleteIcon.classList.add('close', 'icon', 'delete-icon');
    deleteIcon.addEventListener('click', e => {
        todoBox.removeChild(todoCard);
    });

    wrapper.appendChild(input);
    wrapper.appendChild(label);
    todoCard.appendChild(wrapper);
    todoCard.appendChild(deleteIcon);
    todoBox.appendChild(todoCard);

    return todoCard;
};

const reverseTodos = () => {
    const allTodos = Array.from(document.querySelectorAll('.todo-item'));

    while (todoBox.firstChild) {
        todoBox.removeChild(todoBox.firstChild);
    }

    for (const todo of allTodos.reverse()) {
        todoBox.appendChild(todo);
    }

};

dummyBtn.addEventListener('click', e => {
    fetchData('https://koreanjson.com/todos');
});

reverseBtn.addEventListener('click', e => {
    reverseTodos()
});

clearBtn.addEventListener('click', e => {
    while (todoBox.firstChild) {
        todoBox.removeChild(todoBox.firstChild);
    }
});


todoInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
        if (todoInput.value) {
            todoBox.appendChild(createTodo(todoInput.value));
            todoInput.value = null;
        }
    }
});


todoBtn.addEventListener('click', e => {
    if (todoInput.value) {
        todoBox.appendChild(createTodo(todoInput.value));
        todoInput.value = null;
    }
});
};
init();


