import webbrowser
import time

total_break = 3
break_count = 0

print("This progam started on "+time.ctime())
while(break_count < total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=YlUKcNNmywk&list=PLsK0gCOg4x1dqBCUSFXvS14lkHoQQUgEQ&index=1")
    break_count = break_count + 1
