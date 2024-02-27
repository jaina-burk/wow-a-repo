mountains = {'mount everest': {'elevation' : '8848', 'range' : 'himalayas'} ,
             'k2': {'elevation': '8611', 'range' : 'karakoram'},
             'kangchenjunga' : {'elevation' : '8586', 'range' : 'himalayas'},
             'lhotse' : {'elevation': '8516', 'range' : 'himalayas'},
             'makalu' : {'elevation' : '8485', 'range' : 'himalayas'}
             }

for names, elevations in sorted(mountains.items()):
    print('%s is an %s-meter tall mountain, in the %s range.' % (names, elevations['elevation'], elevations['range']))