import redis
import threading
import time
import gevent 
from gevent import monkey
monkey.patch_all()

def callback():
	r = redis.client.StrictRedis()
	sub = r.pubsub()
	sub.subscribe('clock')
	while True:
		for m in sub.listen():
			print m #'Recieved: {0}'.format(m['data'])

def zerg_rush(n):
	for x in range(n):
		t = threading.Thread(target=callback)
		t.setDaemon(True)
		t.start()

def main():
	zerg_rush(1000)
	while True:
		print 'Waiting'
		time.sleep(30)
if __name__ == '__main__':
	main()
		
