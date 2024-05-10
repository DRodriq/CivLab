import logging
import json
import threading
import time
from queue import Queue

# Configure logging
logging.basicConfig(
    filename='events.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Event:
    def __init__(self, event_type, data):
        self.timestamp = time.time()
        self.event_type = event_type
        self.data = data

def log_event(event):
    logging.info(json.dumps(event.__dict__)) 

event_queue = Queue()

def logging_worker():
    while True:
        event = event_queue.get()
        log_event(event)
        event_queue.task_done() 

logging_thread = threading.Thread(target=logging_worker, daemon=True)
logging_thread.start()