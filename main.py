import random
import time
#import simpleaudio 
#print('\a')
#import winsound
#frequency = 2500  # Set Frequency To 2500 Hertz
#duration = 1000  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)

### functions

def user_input(request):
  while True:
    num = input(request)
    try:
        val = int(num)
        if val >= 0:
          break;
        else:
          print('Input should be a positive integer (or 0).')
    except ValueError:
          print("This is not an integer number. Please enter a valid number (0 or greater).")
  return val

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

index_diff = user_input('Choose difficulty on a scale of 1 (Easy) to 5 (Hard): \n')-1

diff_scale = [5, 10, 15, 20, 25]
full_scale = [30, 45, 60, 90, 120]
full = full_scale[index_diff]
diff = diff_scale[index_diff]

print('Thank you for selecting a difficulty level! It will remain memorised until the session is over. \n')

exercise_list = []
f = open("!exercise_list.txt", "r")
exercise_list = f.readlines()
f.close()
separator = exercise_list.index('!!!\n')
group_A = exercise_list[0:separator]
group_B = exercise_list[separator+1:]
#print(group_B[0][:-1],group_B[3])
new_match = 1
timer = 1
while(new_match >= 1):
  new_match = 0
  rank = user_input('Rank last match: ')
  kills = user_input('Kills last match: ')
  assists = user_input('Assists last match: ')
  knocks = user_input('Knocks last match: ')
  
  if(rank == 1):
    print('\n','You are spared!')
  else:
    dkills = max(1, diff-kills)
    dassists = max(1, diff-assists)
    dknocks = max(1, diff-knocks)
    random.shuffle(group_A)
    print('\n')
    print('Exercises for this round: \n')
    print(rank, 'x', group_A[0][:-1], ' .....for your rank \n')
    print(dkills, 'x', group_A[1][:-1], ' .....for your kills \n')
    print(dassists, 'x', group_A[2][:-1], ' .....for your assists \n')
    print(dknocks, 'x', group_A[3][:-1], ' .....for your knocks \n')
    random.shuffle(group_B)
    print('If you had a full team:  ', group_B[0][:-1], ' for', full, 'sec \n')
    print('If you died first:  ', group_B[2][:-1], ' for', full, 'sec \n')
  while timer==1:
    full_timer_question = str(full) + ' sec timer? -> 1 \n     No? -> 0 \n'
    timer = user_input(full_timer_question)
    countdown(full)
  new_match = user_input('New match? -> 1 \n Quitting? -> 0 \n')

exit()