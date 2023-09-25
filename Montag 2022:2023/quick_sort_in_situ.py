import random

def quick_sort_in_situ_h(liste, start, ende) :
    if start == ende:
        return
    pivot = liste[start]
    l = start + 1
    r = ende
    while l < r:
        while l < r and liste[l] <= pivot:
            l += 1
        while r > l and liste [r] >= pivot:
            r -= 1
        liste[l], liste[r] = liste[r], liste[l]
    liste[l - 1], liste[start] = liste[start], liste[l - 1]
    if liste[l-1] > liste[l]:
        liste[l-1], liste[l] = liste[l], liste[l - 1]
    for i in range(start, l-1):
        if liste[i] > pivot:
            print("Fehler: ",  liste )
    for i in range (l, ende + 1):
        if liste[i] < pivot:
            print("Fehler: ", liste)
    quick_sort_in_situ_h(liste, start, l - 1)
    quick_sort_in_situ_h(liste , l, ende)

def quick_sort_in_situ(liste : list):
    quick_sort_in_situ_h(liste, 0, len(liste) - 1)

for i in range(10000000):

    liste : list = [random.randint(0,1000) for i in range(1000)]

    quick_sort_in_situ(liste)

    print(liste)

    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            print("Fehler")
            break