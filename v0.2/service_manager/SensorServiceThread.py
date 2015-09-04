import os, time
import threading, Queue

class SensorThread(threading.Thread):
	
	sensorType = ''
	samplingRate = '1000'

    def __init__(self, dir_q, result_q, sensorType, samplingRate):
        super(WorkerThread, self).__init__()
        self.dir_q = dir_q
        self.result_q = result_q
        self.stoprequest = threading.Event()
        self.sensorType = sensorType
        self.sensorRate = samplingRate

    def run(self):
        while not self.stoprequest.isSet():
            try:
				if sensorType == 'DHT11':
					sensorValue = self.getDht11()
					sleep(samplingRate)
                ## dirname = self.dir_q.get(True, 0.05)
                ## filenames = list(self._files_in_dir(dirname))
                self.result_q.put((self.name, sensorValue))
            except Queue.Empty:
                continue

    def join(self, timeout=None):
        self.stoprequest.set()
        super(WorkerThread, self).join(timeout)

	def getDht11(self):
		return 0
		
		

    def _files_in_dir(self, dirname):
        for path, dirs, files in os.walk(dirname):
            for file in files:
                yield os.path.join(path, file)
