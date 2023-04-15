from django.shortcuts import render, redirect
from .forms import InputForm
from .models import TodoList
from .service import getMaxOrderNum, get_order_num


# Create your views here.
def index(request):
    todos_list = TodoList.objects.all().order_by('order_num')

    form_input = InputForm()
    # print(request.POST)
    if request.method == 'POST':
        if '↑' in request.POST.values() or '↓' in request.POST.values() or '☓' in request.POST.values():

            action, work_entry = get_order_num(request.POST.dict())
            work_entry = int(work_entry)

            print("...:")
            print(TodoList.objects.all().count())

            if action == '↑' and work_entry != 0:
                entry_to_up = TodoList.objects.get(order_num=work_entry)
                entry_to_down = TodoList.objects.get(order_num=work_entry - 1)
                while not entry_to_down:
                    work_entry -= 1
                    entry_to_down = TodoList.objects.get(order_num=work_entry - 1)
                print(f'Founded order_num to downing: {entry_to_down.order_num}')
                entry_to_up.order_num, entry_to_down.order_num = entry_to_down.order_num, entry_to_up.order_num
                try:
                    entry_to_up.save()
                    entry_to_down.save()
                except:
                    print('Database writing error!')


            if action == '↓' and work_entry != TodoList.objects.all().count() - 1:
                entry_to_down = TodoList.objects.get(order_num=work_entry)
                entry_to_up = TodoList.objects.get(order_num=work_entry + 1)
                while not entry_to_up:
                    work_entry += 1
                    entry_to_up = TodoList.objects.get(order_num=work_entry + 1)
                print(f'Founded order_num to downing: {entry_to_up.order_num}')
                entry_to_up.order_num, entry_to_down.order_num = entry_to_down.order_num, entry_to_up.order_num
                try:
                    entry_to_up.save()
                    entry_to_down.save()
                except:
                    print('Database writing error!')

            if action == '☓':
                del_entry = TodoList.objects.filter(order_num=work_entry)
                try:
                    del_entry.delete()
                except:
                    print('Database writing error!')



            if 'btn_add_entry' in request.POST:
                # POST submitted. Processing submitted data.
                form_input = InputForm(request.POST)
                if form_input.is_valid():
                    new_entry = TodoList(
                        todo_text=form_input.cleaned_data['todo_text'],
                        order_num=getMaxOrderNum(TodoList))
                    new_entry.save()
                return redirect('TODOlist_app:index')

    context = {'todos_list': todos_list, 'form_input': form_input}

    return render(request, 'TODOlist_app/index.html', context)