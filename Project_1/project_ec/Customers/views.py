from django.shortcuts import render


def show_account(request):
    return render(request, 'account.html')