import ThingESP

thing = ThingESP.Client('username', 'project_name', 'credentials')

def handleResponse(query):
    if query == 'hi':
        return "Hi there"
    else:
      return 'Your query was invalid..'


thing.setCallback(handleResponse)

thing.start() # this will start ThingESP's own thread..
