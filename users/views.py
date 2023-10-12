from django.views import View
from users.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect



class Register(View):

  template_name = 'registration/register.html'  

# шаблон передаем в форму
  def get(self, request):
    context = {
      'form': UserCreationForm()  
    }

# уже существующая на джанго форма UserCreationForm
# vozvrashaem render shablona
    return render(request, self.template_name, context)
  
  def post(self, request):
    form = UserCreationForm(request.POST)
    #peredatj dannie v formu kotorie nam prishli v requeste v poste

    #proveritj estj li nasha forma, esli dannie validnie, to mozem sohranitj polzovatela
    if form.is_valid():
        form.save()
        #nuzno polu4itj login i parol polzovatela
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        #polu4itj polzovatela s bazi dannih
        user = authenticate(username=username, password=password) #funkcija django
        #использовать ее для аутентификации пользователя, передав имя пользователя и пароль, проверить, 
        # был ли пользователь успешно аутентифицирован. 
        #zaloginitj nahego polzovatelja
        login(request, user)
        #функц login для входа пользователя в систему, 
        # передав объект пользователя и объект запроса (request).
        return redirect('home')
        #perenapravlienije na gl stranicu

    #esli dannie ne validnie, to nuzno formu vernutj v shablon
    context = {
      'form': form
    }
    return render(request, self.template_name, context)