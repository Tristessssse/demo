from django.http import HttpResponse
from django.shortcuts import render

username = {'sxy': 'yyds', 'yzc': 'ljr020520', 'ljr': 'yzc201217', 'yhq': 'yhq761104', 'OUC': '1924'}
gender = {'sxy': 'Miss ', 'yzc': 'Mr. ', 'ljr': 'Miss ', 'yhq': 'Mr. ', 'OUC': ' '}


# Create your views here.


def my_login(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        if username1 in username and password1 == username[username1]:
            return HttpResponse('Welcome!')
        elif username1 not in username and len(username1) != 0:
            error = {'error': 'This username does not exist.'}
            return render(request, 'main.html', error)
        elif username1 in username and password1 != username[username1] and len(password1) != 0:
            error = {'error': 'Your password is incorrect'}
            return render(request, 'main.html', error)
        elif len(username1) == 0 or len(password1) == 0:
            error = {'error': "The forms musn't be blank"}
            return render(request, 'main.html', error)
        # return render(request,'main.html',dict)


def my_register(request):
    if request.method == 'GET':
        return render(request, 'main2.html')
    elif request.method == 'POST':
        usernameA = request.POST.get('usernameA')
        passwordA = request.POST.get('passwordA')
        passwordB = request.POST.get('passwordB')
        if len(usernameA) < 16 and len(passwordA) < 16 and len(passwordB) < 16 and \
                len(usernameA) != 0 and len(passwordA) != 0 and len(passwordB) != 0:
            if passwordA == passwordB:
                for i in usernameA or passwordA:
                    if i.isdigit() or i.isalpha() and not '\u4e00' <= i <= '\u9fff':
                        if usernameA not in username:
                            username[usernameA] = passwordA
                            success = {'success': "Registration successful!"}
                            return render(request, 'main2.html', success)
                        else:
                            error = {'error': "The username has already existed!"}
                            return render(request, 'main2.html', error)

                    else:
                        error = {'error': "The username or password you entered contains illegal characters！"}
                        return render(request, 'main2.html', error)
            else:
                error = {'error': "The two passwords you entered must be the same！"}
                return render(request, 'main2.html', error)
        else:
            error = {'error': "The length of the character you entered is illegal."}
            return render(request, 'main2.html', error)
