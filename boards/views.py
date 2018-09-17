from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    # board_name = list()

    # for board in boards:
    #     board_name.append(board.name)
    #     board_name.append(board.description)
    # return HttpResponse(board_name)