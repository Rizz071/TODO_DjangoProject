from django.shortcuts import render, redirect
from .forms import InputForm, addListForm, delListForm
from .models import TodoList, TodoTitle
from .service import getMaxOrderNum


# Create your views here.
def index(request):
    overall_list = {}
    for title in TodoTitle.objects.all():
        overall_list[title] = list(title.todolist_set.all())

    form_input = InputForm()

    if request.method == 'POST':
        # Whats consists in request.POST
        print(request.POST)

        # Converting QueryDict to list and retrieve second element. It is str type.
        query_dict_to_list = list(request.POST)[1]

        # Extracting action type
        action = request.POST.get(query_dict_to_list)

        if '↑' in action or '↓' in action or '☓' in action:

            title_id = query_dict_to_list.split(",")[0]

            work_entry_num = int(query_dict_to_list.split(",")[1])

            print("title_id =", title_id, "entry =", work_entry_num, "action =", action)

            work_title = TodoTitle.objects.get(id=title_id)
            print("Work title object =", work_title)
            work_entry = work_title.todolist_set.get(order_num=work_entry_num)
            print("Work todo object =", work_entry)

            if action == '↑' and work_entry_num != 0:
                entry_to_up = work_title.todolist_set.get(order_num=work_entry_num)
                entry_to_down = work_title.todolist_set.get(order_num=work_entry_num - 1)
                while not entry_to_down:
                    work_entry_num -= 1
                    entry_to_down = work_title.todolist_set.get(order_num=work_entry_num - 1)
                print(f'Founded order_num to downing: {entry_to_down.order_num}')
                entry_to_up.order_num, entry_to_down.order_num = entry_to_down.order_num, entry_to_up.order_num
                try:
                    entry_to_up.save()
                    entry_to_down.save()
                except:
                    print('Database writing error!')
                return redirect('TODOlist_app:index')

            if action == '↓' and work_entry_num != work_title.todolist_set.all().count() - 1:
                entry_to_down = work_title.todolist_set.get(order_num=work_entry_num)
                entry_to_up = work_title.todolist_set.get(order_num=work_entry_num + 1)
                while not entry_to_up:
                    work_entry_num += 1
                    entry_to_up = work_title.todolist_set.get(order_num=work_entry_num + 1)
                print(f'Founded order_num to downing: {entry_to_up.order_num}')
                entry_to_up.order_num, entry_to_down.order_num = entry_to_down.order_num, entry_to_up.order_num
                try:
                    entry_to_up.save()
                    entry_to_down.save()
                except:
                    print('Database writing error!')
                return redirect('TODOlist_app:index')

            if action == '☓':
                del_entry = work_title.todolist_set.get(order_num=work_entry_num)
                print("Deleting todo string: ", del_entry.todo_text)
                try:
                    del_entry.delete()
                except:
                    print('Database writing error!')
                return redirect('TODOlist_app:index')

        if 'todo_text' in query_dict_to_list:
            # Adding entry to TODO_list
            query_dict_to_list = list(request.POST)[2]
            title_name = query_dict_to_list.split(",")[1]

            # Getting id of title
            title_object = TodoTitle.objects.get(title=title_name)
            print(title_object.id)

            form_input = InputForm(request.POST)
            if form_input.is_valid():
                new_entry = TodoList(
                    todo_text=form_input.cleaned_data['todo_text'],
                    order_num=getMaxOrderNum(TodoList, title_object),
                    title=title_object)
                new_entry.save()
            return redirect('TODOlist_app:index')

    context = {'overall_list': overall_list, 'form_input': form_input}
    return render(request, 'TODOlist_app/index.html', context)


def add_list(request):
    if request.method == 'GET':
        form_addListForm = addListForm()

    if request.method == 'POST':
        form_addListForm = addListForm(data=request.POST)

        try:
            form_addListForm.save()
        except:
            print('Database writing error!')
        return redirect('TODOlist_app:index')

    context = {'form_addListForm': form_addListForm}
    return render(request, 'TODOlist_app/add_list.html', context)


def del_list(request):
    if request.method == 'GET':
        form_delListForm = delListForm()

    if request.method == 'POST':
        form_delListForm = delListForm()
        title_name_to_del = request.POST.get('title')

        try:
            TodoTitle.objects.get(title=title_name_to_del).delete()
        except:
            print('Database writing error!')
        return redirect('TODOlist_app:index')

    context = {'form_delListForm': form_delListForm, 'titles': TodoTitle.objects.all()}
    return render(request, 'TODOlist_app/del_list.html', context)
