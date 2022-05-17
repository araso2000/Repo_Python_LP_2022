offset = 1
print(offset)
offset = "\n"
print(offset)
offset = [1, 1]
print(offset)

booleano = False
print(booleano)


jenkins_message = ("[LOG] Testing geolocation APIs...\n"
"[LOG] Getting access to OpenStreetMap. \n"
"[LOG] Connection established."
"[LOG] Getting geolocation data from OpenStreetMaps.\n"
"[LOG]: Response receive. Parsing JSON response...\n"
"[ERROR]: JSON.parse: bad parsing...\n"
"[LOG] Getting data from Google maps...\n"
"...\n")
index = jenkins_message.lower().find("[error]")
error_line = jenkins_message[index:].splitlines()[1]
print (error_line)