days = ('- first second third fourth fifth sixth '
        'seventh eighth ninth tenth eleventh twelfth'.split())

gifts = [
    'twelve Drummers Drumming, ',
    'eleven Pipers Piping, ',
    'ten Lords-a-Leaping, ',
    'nine Ladies Dancing, ',
    'eight Maids-a-Milking, ',
    'seven Swans-a-Swimming, ',
    'six Geese-a-Laying, ',
    'five Gold Rings, ',
    'four Calling Birds, ',
    'three French Hens, ',
    'two Turtle Doves, ',
    'and a Partridge in a Pear Tree.'
]


def verse(N):
    output = f'On the {days[N]} day of Christmas my true love gave to me: '
    for i in range(12 - N, 12):
        output += f'{gifts[i]}'
    return output.replace('and ', '') if N == 1 else output


def recite(a, b):
    output = []
    for i in range(a, b + 1):
        output.append(verse(i))
    return output

print(recite(1, 12))
