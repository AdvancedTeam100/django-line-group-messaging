from django.shortcuts import render, redirect
from .forms import ManagerForm
from .models import Manager
from django.http import HttpResponseBadRequest, HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

line_bot_api = LineBotApi("/ZFZoI1+zmOo0g9TZy4FpyGxhoVVec7tbYXve3QQzV70p276Qo5/MFq5d+sciP2xbEmBV2NVPEx6lbEDld2gkBikVxQahOLYDrr1z/I0t06X685Bqbvat​​XoiIxfnRip5W2vwOtXoJqKYty iS4HiyRwdB04t89/1O/w1cDnyilFU=")
line_handler = WebhookHandler("c14a13ebf36bfac9da8446f256e246b9")

# Add Blog

def create_member(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = ManagerForm()
    return render(request, 'create.html', {'form':form})

# retrieve blog

def retrieve_member(request):
    members = Manager.objects.all()
    return render(request,'search.html',{'members':members} )

# Update Blog

def update_member(request,pk):
    members = Manager.objects.get(id=pk)
    form = ManagerForm(instance=members)

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=members)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'blogs': members,
        'form': form,
    }
    return render(request,'update.html',context)

# Delete Blog

def delete_member(request, pk):
    blogs = Manager.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/search')

    context = {
        'blogs': blogs,
    }
    return render(request, 'remove.html', context)

@line_handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_id = event.source.user_id
    message_text = event.message.text

    print(f"Received message from user {user_id}: {message_text}")

def view_message(request):
    line_signature = request.headers['X-Line-Signature']
    try:
        line_handler.handle(request.body.decode('utf-8'), line_signature)
    except InvalidSignatureError:
        return HttpResponseBadRequest()
    
    return render(HttpResponse(),'messages.html')