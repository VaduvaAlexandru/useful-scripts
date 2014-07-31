import OleFileIO_PL
from struct import unpack
import hashlib
import sys

def rc4_crypt(key, data):
	# prepare key
	S = range(256)
	j = 0
	for i in range(256):
		j = (j + S[i] + ord(key[i % len(key)])) % 256
		S[i], S[j] = S[j],S[i]
	
	# encrypt/decrypt
	i = j = 0
	out = ""
	for c in data:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j],S[i]
		out += chr(ord(c) ^ S[(S[i] + S[j]) % 256])
	return out

def find_rc4_passinfo(stream):
	while True:
		pos = stream.tell()
		if pos >= stream.size:
			break # eof
		type = unpack("<h", stream.read(2))[0]
		length = unpack("<h", stream.read(2))[0]
		data = stream.read(length)
		
		if type == 0x2f: # FILEPASS
			if data[0:6] == '\x01\x00\x01\x00\x01\x00':
				#print "found rc4 structure"
				data = data[6:]
				salt = data[:16]
				verifier = data[16:32]
				verifierHash = data[32:48]
				return (salt, verifier, verifierHash)
				
	return None
				
def gen_excel_real_key(pwd, salt):
	h0 = hashlib.md5(pwd).digest()
	h1 = hashlib.md5((h0[:5] + salt) * 16).digest()
	return h1[:5]
			
def test_pass(pwd, salt, verifier, verifierHash):
	real_key = gen_excel_real_key(pwd, salt)
	key = hashlib.md5(real_key + '\x00\x00\x00\x00').digest()
	dec = rc4_crypt(key, verifier + verifierHash)
	if hashlib.md5(dec[:16]).digest() == dec[16:]:
		print "valid pass"
	else:
		print "invalid pass"

	
if len(sys.argv) != 3:
	print "Usage: %s <xls file> <password>" % sys.argv[0]
	sys.exit(1)
	
xlsfile = sys.argv[1]

# Test if a file is an OLE container:
if not OleFileIO_PL.isOleFile(xlsfile):
	print "Invalid XLS file"
	sys.exit(1)

# Open OLE file:
ole = OleFileIO_PL.OleFileIO(xlsfile)

workbookStream = ole.openstream('Workbook')
if workbookStream == None:
	print "Invalid XLS file"
	sys.exit(1)
	
passinfo = find_rc4_passinfo(workbookStream)
if passinfo == None:
	print "Cannot find RC4 pass info"
else:
	pwd = sys.argv[2].encode('utf-16')[2:]
	test_pass(pwd, *passinfo)
workbookStream.close()
