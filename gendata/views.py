from django.shortcuts import redirect, render
import openai

openai.api_key = "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"
# Create your views here.
def index(request):
    return render(request, 'index.html')

def prompt(request):
    return render(request, 'prompt.html')

def generate_rsa(request):
    prompt = request.POST.get('rsa_prompt')
    
    messages = []
    messages.append({"role": "system", "content": "Your name is Karabo. You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    
    response = response['choices'][0]['message']['content']
    print("Resonse====================================================: ", response)
    
    return redirect('gendata:index')

def generate_sitelink(request):
    pass