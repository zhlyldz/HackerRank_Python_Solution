Write a Function
Soru Linki;
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leep = False
    if year %4==0:
        leep =True
    if year %100==0:
        leep=False
    if year %400 == 0:
        leep=True

    return leep

year = int(input())
print(is_leap(year))
