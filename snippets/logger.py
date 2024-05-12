import json
import numpy as np
import sys

# Example event data
events = []

def log_event(time, agent_id, action, location, result):
    event = {
        "time": time, 
        "agent_id": agent_id,  
        "action": action, 
        "location": list(location), 
        "result": result
    }
    events.append(event)
   
#Example usage:
np.random.seed(0)
for _ in range(3):
    time = np.random.rand()
    agent_id = f"a{np.random.randint(100, 999)}"
    action = np.random.choice(["move", "pickup", "drop", "invalid_action"])
    location = tuple(np.random.rand(2) * 10)
    print(sys.getsizeof(location))
    result = np.random.choice(["success", "fail", "object_found"], p=[0.8,0.1,0.1])
    log_event(time, agent_id, action, location, result)

print(events)