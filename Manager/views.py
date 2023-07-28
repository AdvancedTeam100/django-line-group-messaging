from django.shortcuts import render, redirect
from .forms import ManagerForm
from .models import Manager
from .models import Message
from django.http import HttpResponseBadRequest, HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
from django.views.decorators.csrf import csrf_exempt


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

# Retrieve Blog
def retrieve_member(request):
    members = Manager.objects.all()
    return render(request,'search.html',{'members':members} )

# Update Blog
def update_member(request, pk):
    member = Manager.objects.get(id=pk)
    form = ManagerForm(instance=member)

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'member': member,
        'form': form,
    }
    return render(request,'update.html',context)

# Delete Blog
def delete_member(request, pk):
    member = Manager.objects.get(id=pk)

    if request.method == 'POST':
        member.delete()
        return redirect('/search')

    context = {
        'member': member,
    }
    return render(request, 'remove.html', context)

@line_handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_id = event.source.user_id
    message_text = event.message.text

    print(f"Received message from user {user_id}: {message_text}")
    handle_message(message_text, user_id)
    return HttpResponse("test!!")


@csrf_exempt # this is used for avoid csrf request from line server
def callback(request):
    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        global domain
        domain = request.META['HTTP_HOST']
        
        # get request body as text
        body = request.body.decode('utf-8')
        # handle webhook body
        try:
            line_handler.handle(body, signature)
            
            message_text = body['events'][0]['message']['text']
            sender_id = body['events'][0]['source']['userId']
            handle_message(message_text, sender_id)
        except InvalidSignatureError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def handle_message(message, sender_id):

    # Create a new instance of the Message model to store the message
    new_message = Message(
        sender_id=str(sender_id),
        receiver_id='RECEIVER_ID',  # Replace with actual receiver ID
        content=message
    )
    new_message.save()