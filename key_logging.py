# from pynput.keyboard import Key, Listener
# import logging

# logging.basicConfig(filename = ('log_results.txt'),level = logging.DEBUG, format = '%(asctime)s : %(message)s')
# def keypress(Key):
#     logging.info(str(Key))
# with Listener(on_press = keypress) as listener:
#      listener.join()


from threading import Thread

def run1():
	while(True):
		print("Inside Thread")

def run2():
	while(True):
		print("Inside Thread number 2")

thread = Thread(target=run1)
thread.start()
thread2 = Thread(target=run2)
thread2.start()
# run1()

while(True):
	print("Outside Thread")



