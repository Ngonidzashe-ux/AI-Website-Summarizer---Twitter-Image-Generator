import requests

#Send a get request to the url running our flask server, include the query parameter service.
#The flask route, /tweets expects some dynamic content and the service parameter is a way to provide that content 
response = requests.get('http://127.0.0.1:5000/tweets?service=sagemaker')
response.text
#When you make an HTTP request using requests, the server sends back a response, and response.text allows you to access the textual content of that response.
