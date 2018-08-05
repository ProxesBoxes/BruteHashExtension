import hashpumpy
import base64

print("Welcome to the Hash Extension brute force tool")
print("a tool for The Information Technology Syndicate\n")

print("Original Digest (in hex):")
hexdigest = raw_input()
print("Original Data (in ASCII):")
original_data = raw_input()
print("Data to Add (in ASCII):")
data_to_add = raw_input()
print("Starting Key Length:")
key_length_start = int(raw_input())
print("Ending Key Length:")
key_length_end = int(raw_input())+1

for key_length in range (key_length_start, key_length_end):
    
    out = hashpumpy.hashpump( hexdigest, original_data, data_to_add, key_length)
    digest = out[0]
    message = out[1]
    query = base64.b64encode(message)
    newKey = base64.b64encode(digest.decode("hex"))
    print("--------------------------------")
    print("Key len:" +str(key_length))
    print("Query: "+message)
    print("Digest: "+digest)
    print("<query base64> <new digest>:")
    print(query+" "+newKey)
