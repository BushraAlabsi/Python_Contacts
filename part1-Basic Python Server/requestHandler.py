from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

 #This class will handle any incoming request from
 #the browser 

class myHandler(BaseHTTPRequestHandler):
	#This will handle GET requests
	def do_GET(self):
		# Add the outgoing status here
		print("Goodbye, World!")
		# You will need to change this if you are sending something
  		# other than plain text, like JSON or HTML.
  		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("<html><head><title>Python Sprint</title></head>")
		self.wfile.write("<body><p>Hello World</p>")
		self.wfile.write("</body></html>")
		

		# Send the "Hello World" message here 
		
		return