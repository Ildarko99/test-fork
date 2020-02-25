time = int(input('Input seconds \n'))
hours = (time // 3600)
minutes = time // 60 % 60
sec = time % 60
if sec < 10:
    sec = '0' + str(sec)
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)

print(f'{hours}:{minutes}:{sec}')

