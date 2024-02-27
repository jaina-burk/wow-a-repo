mountains = {'mount everest': '29029',
             'k2': '28251',
             'kangchenjunga' : '28169',
             'lhotse' : '27940',
             'makalu' : '27838'
             }

for names in sorted(mountains.keys()):
    print("%s is %s feet tall." % (names.title(), mountains[names]))