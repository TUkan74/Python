from datetime import date

casy = input().split()

zaciatok = casy[0:3] 

koniec = casy[3::]

start = date(int(zaciatok[2]), int(zaciatok[1]), int(zaciatok[0]))
end = date(int(koniec[2]), int(koniec[1]), int(koniec[0]))
delta = end - start
print(delta.days)