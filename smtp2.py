from socket import *
import ssl


mailserver = ("smtp.gmail.com", 465)
sslSocket = socket(AF_INET, SOCK_STREAM);
sslSocket = ssl.wrap_socket(sslSocket, ssl_version=ssl.PROTOCOL_SSLv23)
sslSocket.connect(mailserver)
receipients_list = []
bcc_list = []
cc_list = []
filename = raw_input("Enter file name to read from\n")
s = raw_input("Enter subject\n")
subject = 'Subject: '+ s +'\r\n'
n = input("Enter no of receipients\n")
for i in range(int(n)):
	s = raw_input("Enter receipient"+str(i+1)+"\n")
	receipients_list.append("<"+s+">")

print receipients_list
n = input("Enter no of cc receipients\n")
for i in range(int(n)):
	s = raw_input("Enter cc receipient"+str(i+1)+"\n")
	cc_list.append("<"+s+">")
print cc_list
n = input("Enter bcc list\n")
for i in range(int(n)):
	s = raw_input("Enter bcc receipient"+str(i+1)+"\n")
	bcc_list.append("<"+s+">")
print bcc_list
sslSocket.send("EHLO\r\n")
print sslSocket.recv(4096)
sslSocket.send("AUTH LOGIN\r\n")
print sslSocket.recv(4096)
sslSocket.send("email_id")
print sslSocket.recv(4096)
sslSocket.send("password")
print sslSocket.recv(4096)
sslSocket.send("MAIL FROM:<anurag>\r\n")
print sslSocket.recv(4096)
for i in receipients_list:
	sslSocket.send("RCPT TO:"+i+"\r\n")
#print sslSocket.recv(4096)
for i in cc_list:
	sslSocket.send("RCPT TO:"+i+"\r\n")
for i in bcc_list:
	sslSocket.send("RCPT TO:"+i+"\r\n")
print sslSocket.recv(4096)
sslSocket.send("DATA\r\n")
print sslSocket.recv(4096)
sslSocket.send(subject)
sslSocket.recv(4096)
sslSocket.send("CC: "+",".join(cc_list) + "\r\n")
sslSocket.send("TO: "+",".join(receipients_list)+"\r\n")
sslSocket.send("mailer: "+",".join(bcc_list)+"\r\n")
#print sslSocket.recv(4096)
f = open(filename,'r')
for i in f.readlines():
	sslSocket.send(i+"\r\n")
#print sslSocket.recv(4096)
#print sslSocket.recv(4096)
sslSocket.send("\r\n.\r\n")
print sslSocket.recv(4096)
sslSocket.send("QUIT\r\n")
print sslSocket.recv(4096)

#commands ,timeout times, return codes,error msgs
'''

	{command_INIT,          0,     5*60,  220, ECSmtp::SERVER_NOT_RESPONDING},
	{command_EHLO,          5*60,  5*60,  250, ECSmtp::COMMAND_EHLO},
	{command_AUTHPLAIN,     5*60,  5*60,  235, ECSmtp::COMMAND_AUTH_PLAIN},
	{command_AUTHLOGIN,     5*60,  5*60,  334, ECSmtp::COMMAND_AUTH_LOGIN},
	{command_AUTHCRAMMD5,   5*60,  5*60,  334, ECSmtp::COMMAND_AUTH_CRAMMD5},
	{command_AUTHDIGESTMD5, 5*60,  5*60,  334, ECSmtp::COMMAND_AUTH_DIGESTMD5},
	{command_DIGESTMD5,     5*60,  5*60,  335, ECSmtp::COMMAND_DIGESTMD5},
	{command_USER,          5*60,  5*60,  334, ECSmtp::UNDEF_XYZ_RESPONSE},
	{command_PASSWORD,      5*60,  5*60,  235, ECSmtp::BAD_LOGIN_PASS},
	{command_MAILFROM,      5*60,  5*60,  250, ECSmtp::COMMAND_MAIL_FROM},
	{command_RCPTTO,        5*60,  5*60,  250, ECSmtp::COMMAND_RCPT_TO},
	{command_DATA,          5*60,  2*60,  354, ECSmtp::COMMAND_DATA},
	{command_DATABLOCK,     3*60,  0,     0,   ECSmtp::COMMAND_DATABLOCK},	
	{command_DATAEND,       3*60,  10*60, 250, ECSmtp::MSG_BODY_ERROR},
	{command_QUIT,          5*60,  5*60,  221, ECSmtp::COMMAND_QUIT},
	{command_STARTTLS,      5*60,  5*60,  220, ECSmtp::COMMAND_EHLO_STARTTLS}
'''
