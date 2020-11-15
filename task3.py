import copy

file = input()
f = open(file, 'r')

counter = 0
MistakeTop = 0
MistakeBot = 0
TryesTop = 0
TryesBot = 0
AmountTop = 0
AmountBot = 0
AmountBlockedTop = 0
AmountBlockedBot = 0

for line in f:
    line.strip()
    if counter == 0:
        continue
    elif counter == 1:
        volume = int(line)
    elif counter == 2:
        now = int(line)
        volume_at_start = copy.copy(now)
    else:
        empty = volume - now
        index = line.index("wanna")
        line = line[index:].rstrip('l').split(' ')
        command = line[1]
        water = int(line[2])
        if command == "top":
            TryesTop += 1
            if water > empty:
                MistakeTop += 1
                AmountBlockedTop += zalit
                continue
            now += zalit
            AmountTop += zalit
        else:
            TryesBot += 1
            if water > now:
                MistakeBot += 1
                AmountBlockedBot += zalit
                continue
            now -= zalit
            AmountBot += zalit

#какое количество попыток налить воду в бочку было за указанный период?
print(TryesTop)
#какой процент ошибок был допущен за указанный период?
MistakeTop = TryesTop / MistakeTop * 100
print(MistakeTop)
#какой объем воды был налит в бочку за указанный период?
print(AmountTop)
#какой объем воды был не налит в бочку за указанный период?
print(AmountBlockedTop)
#какое количество попыток зачерпнуть воду из бочки было за указанный период?
print(TryesBot)
#какой процент ошибок был допущен за указанный период?
MistakeBot = TryesBot / MistakeBot * 100
print(MistakeBot)
#какой объем воды был вылит из бочки за указанный период?
print(AmountBot)
#какой объем воды был не вылит из бочки за указанный период?
print(AmountBlockedBot)
#какой объем воды был в бочке в начале указанного периода? Какой в конце указанного периода?
print(volume_at_start, now)