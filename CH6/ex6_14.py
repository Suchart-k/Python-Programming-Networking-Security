# Encrypted/Decrypted program
# These codes for encrypting message
i = 0
encryptedMsg = []
msg = input("Enter string message :")
while i < len(msg):
    C = ord(msg[i])
    F = 32 + (((212 - 32)/100) * C)
    encryptedMsg.append(F)
    i += 1
print ("Encrypted message : ",encryptedMsg)
#These codes for decrypting message
i = 0
decryptedMsg = ""
while i < len(encryptedMsg):
    F = encryptedMsg[i]
    C = (F - 32) * (100/(212 - 32))
    temp = chr(int(C))
    decryptedMsg = decryptedMsg + str(temp)
    i += 1
print ("Decrypted string : ",decryptedMsg)

