import ThingESP

thing = ThingESP.Client('username', 'project_name', 'credentials')

def handleResponse(query):
    if query == 'hi':
        return 'Hello, whats up'


thing.setCallback(handleResponse).start()
