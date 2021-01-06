import sys  #we need command line arguement
import requests # For making the request
import socket 
import json

#if no argument provided in the command line
if len(sys.argv)< 2:
	print("Usage: " +sys.argv[0] + " <url> " )
	sys.exit(1)
 	
req=requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_=socket.gethostbyname(sys.argv[1])
print("\n The IP Address of "+sys.argv[1]+"is :"+gethostby_+"\n")

#ipinfo is the api which will provide the info

req_two=requests.get("https://ipinfo.io/"+gethostby_+"/json")

resp_=json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])


