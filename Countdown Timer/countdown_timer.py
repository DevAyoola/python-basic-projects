# Countdown Timer

import time

# Countdown function
def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print("Time over!")

# Driver code
if __name__ == "__main__":
    t = input("Enter the number of seconds: ")
    countdown(int(t))
