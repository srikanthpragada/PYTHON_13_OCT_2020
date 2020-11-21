import threading

print(threading.main_thread())

class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 26):
            print(f'Child : {i}')


print("Main Thread")
pt = PrintThread()
pt.start()

for i in range(1, 26):
    print(f'Main : {i}')
