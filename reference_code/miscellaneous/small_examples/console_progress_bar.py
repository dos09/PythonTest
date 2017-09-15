import math
percent = 0
max_bars = 20
bar = '#'
dot = '.'
while not percent > 1:
    bars_count = math.ceil(max_bars * percent)
    dots_count = max_bars - bars_count
    print('percent: %4.4s, bars count: %3s/%3s' %
          (percent, bars_count, max_bars))
    print('[%s%s]' % (bar * bars_count, dot * dots_count))
    percent += 0.1
