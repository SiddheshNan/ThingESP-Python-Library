import ThingESP
import time

thing = ThingESP.Client('username', 'project_name', 'credentials')

def handleResponse(query):
    if query == 'hi':
        time.sleep(2)
        return 'Done! Light Turned on'


thing.setCallback(handleResponse).start()
