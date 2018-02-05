#!/usr/bin/python
from __future__ import print_function
import sys
import subprocess

def runCMD(url, expected_httpresponse_code):
  base_cmd = 'curl -s -o /dev/null -w "%{http_code}" '
  cmd = base_cmd + '"' + url + '"'	
  #print (cmd)
  r_code = int(subprocess.Popen(cmd,shell=True,stdout = subprocess.PIPE).communicate()[0])		
  if (r_code == expected_httpresponse_code):
    print ("Received Http response code:" + str(r_code) + " ...Test OK")	 	
  else:	
    print ("Received Http response code:" + str(r_code) + " ...Test FAILED")	 	
  

def runtests(base_url):
  print ('Starting tests on  ' + base_url)
  print ()

  #Events by Engineer
  print ("Testing for Events by Engineer")	
  url = base_url + 'name=vincent'	
  print ("Correct Request: ", url)		 	
  runCMD(url,200)
  url = base_url + 'name='	
  print ("Missing required field(name), Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'namevincent'	
  print ("Bad(missing =) Request: ", url)		 	
  runCMD(url,404)

  print()	  
  #Events between time period
  print ("Testing for Events between a begin and end time")	
  url = base_url + 'events?start_date=20171101&start_time=01:01:01&end_date=20171101&end_time=22:10:01'	
  print ("Correct Request: ", url)		 	
  runCMD(url,200)
  url = base_url + 'events?start_date=20171101&start_time=01:01:01&end_time=22:10:01'	
  print ("Missing required field(end_date), Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'events?start_date=201101&start_time=01:01:01&end_date=20171101&end_time=22:10:01'	
  print ("Invalid Date(start_date), Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'events?start_date=20112401&start_time=01:01:01&end_date=20171101&end_time=22:10:01'	
  print ("Invalid Date(start_date), Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'events?start_date=201101&start_time=01:91:01&end_date=20171101&end_time=22:10:01'	
  print ("Invalid Time(start_time), Request: ", url)		 	
  runCMD(url,404)

  print()	 
  #Summary of Event statistics
  print ("Testing for Event summary by date")	
  url = base_url + 'summary/date=20170101'
  print ("Correct Request: ", url)		 	
  runCMD(url,200)
  url = base_url + 'summary/date20170101' 
  print ("Invalid Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'summary/date=20174501' 
  print ("Invalid Date, Request: ", url)		 	
  runCMD(url,404)
  url = base_url + 'summary/date=201501' 
  print ("Invalid Date, Request: ", url)		 	
  runCMD(url,404)
 
  print()
  #List all engineers in our data set
  print ("Listing all engineers in our dataset")
  url = base_url + 'engineers'
  print ("Correct Request: ", url)
  runCMD(url,200)
  url = base_url + 'engine'
  print ("Invalid Request: ", url)
  runCMD(url,404)

 




def main():
  if (len(sys.argv) != 2):
    print ("Usage: ./testScript.py <hostname>")
    print ("No hostname provided, assuming default 54.172.96.124")
    hostname = "54.172.96.124"	
  else:
    hostname = sys.argv[1]
  BASE_URL = 'http://' + hostname + '/events/'
  runtests(BASE_URL)	

if __name__ == "__main__":
  main()
  sys.exit(0)	
