from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template

from classes.data import Data

DATA = Data.load_default_settings()
# from django.conf import settings

# import views

# def titlescreen(request):
#     return render(request, 'titlescreen.html')

def titlescreen(request):
    key = request.GET.get("key", None)
    if (key is not None):
        if (key == 'button1'):
            return redirect("moviemon/worldmap")
        elif (key == "button2"):
            return redirect("moviemon/load_game")
    return render(request, "titlescreen.html")

def worldmap(request):
    key = request.GET.get("key", None)
    pos = DATA.map.map[DATA.pos[0]][DATA.pos[1]]
    data= {"x": str(DATA.pos[1] * 29), "y": str(DATA.pos[0] * 29), 
    "score": str(DATA.moviballs),
    "msg": ""}
    if (key is not None):
        if (key == "right" and DATA.pos[1] < 9):
            data["x"] = str(int(data["x"]) + 29)
            DATA.pos[1] += 1
        if (key == "left" and DATA.pos[1] > 0):
            data["x"] = str(int(data["x"]) - 29)
            DATA.pos[1] -= 1
        if (key == "up" and DATA.pos[0] > 0):
            data["y"] = str(int(data["y"]) - 29)
            DATA.pos[0] -= 1
        if (key == "down" and DATA.pos[0] < 9):
            data["y"] = str(int(data["y"]) + 29)
            DATA.pos[0] += 1
        if (pos == 2):
            msg="You find Moviemon. Push A for Battle"
        if (pos == 3):
            msg="Congrats! You find movieball"
            DATA.moviballs +=1
            data["score"] = DATA.moviballs
            DATA.map.map[DATA.pos[1]][DATA.pos[0]] = 0
        if (key == 'start'):
            return redirect("moviemon/options")
        elif (key == "button2"):
            return redirect("moviemon/moviedex")
    return render(request, 'worldmap.html', data)

def battle(request):
    
    return render(request, 'battle.html')

def load_game(request):
    return render(request, 'load.html')
    
def moviedex(request):
    return render(request, 'moviedex.html')

def save(request):
    key = request.GET.get("key", None)
    data = {"colorA": "blue", "colorB": "gray", "colorC": "gray",
    "contA": "Free", "contB": "Free", "contC": "Free"}
    if (key is not None):
    #     if (key == "down"):
    #         pos += 1
    #     if (key == "up"):
    #         pos -=1
    #     if (pos%3) == 0:
    #         data["colorA"] = "blue"
    #     if (pos % 3) == 1:
    #         data["colorB"] = "blue"
    #         data["colorA"] = "gray"
    #     if (pos % 3) == 2:
    #         data["colorC"] = "blue"
    #         data["colorA"] = "gray"
    #     # if (key == 'A'):    
        if (key == "B"):
            return redirect("moviemon/options")
    return render(request, 'save.html', data)

def options(request):
    return render(request, 'options.html')

def detail(request):
    key = request.GET.get("key", None)
    if (key is not None):
        if (key == 'start'):
            return redirect("moviemon/worldmap")
        elif (key == "button1"):
            return redirect("moviemon/options/save_game")
        elif (key == "button2"):
            return redirect("moviemon/")
    return render(request, 'detail.html')