1
from itapp.core1.core import Core
from itapp.core1.llm_models.llm_models import LLM
from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .models import ChatMessage

def chatbot_view(request):
    return render(request, 'chatbot.html')

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # پردازش پیام و ارسال به مدل هوش مصنوعی
        # response = process_message_with_ai(message)
        # ذخیره پیام و پاسخ در دیتابیس
        # ChatMessage.objects.create(user_message=message, bot_response=response)
        # return JsonResponse({'response': response})
    return redirect('chatbot')

def view1(request):
    # کد مربوط به ویو 1
    pass

def view2(request):
    # کد مربوط به ویو 2
    pass

def view3(request):
    # کد مربوط به ویو 3
    pass


def home(request):
    core = Core()
    core.load_topic()
    core.create_session()

    return render(request, "home.html", core.context)


def chat(request, query):
    core = Core()
    core.add_url(query=query)
    if core.query_has_any("chat"):
        core.add_context(key="question", val=request.POST.get("Question"))
        llm = LLM(model_name=core.context.get("model"))
        core.add_context(key="answer", val=llm.chat(request.POST.get("Question")))

    return render(request, "chat.html", core.context)

from django.shortcuts import render
from .forms import SQLQueryForm

def sql_editor(request):
    if request.method == 'POST':
        form = SQLQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # در اینجا می‌توانید کوئری را پردازش کنید (مثلاً اجرا در دیتابیس)
            print("Query received:", query)
    else:
        form = SQLQueryForm()

    return render(request, 'sql_editor.html', {'form': form})