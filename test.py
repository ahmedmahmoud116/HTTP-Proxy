line_elements = "head /hypertext/WWW/TheProject.html HTTP/1.1"
"Host: info.cern.ch"
line_elements = line_elements.rstrip()
line = line_elements.split(" ")
l = "http://google.com:8080"
host_and_port_array = l.split('://')
print(host_and_port_array)
host_and_port = host_and_port_array[1]
print(host_and_port)
host_and_port_array = host_and_port.split(':')
print(host_and_port_array)
port = host_and_port_array[1]
print(port)
host_and_path = host_and_port_array[0]
print(host_and_path)
host_and_path_array = host_and_path.split('/',1)
print(host_and_path_array)
host = host_and_path_array[0]
if(len(host_and_path_array) == 2):
    path = "/" + host_and_path_array[1]
else:
    path = "/"
print(host)
print(path)

port_url = '80/'
url = ''
if(port_url.endswith('/')):
    port = port_url.split('/')[0]
    url = '/' + port_url.split('/')[1]
print(port)
print(url)
"GET /things HTTP/1.0"
"Host: www.google.com:8080"
"Accept: application/json"
"GET info.cern.ch/hypertext/WWW/TheProject.html HTTP/1.1"
