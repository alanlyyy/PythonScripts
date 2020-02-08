import base64

class Encryption:
    """This class is used to store commonly used encrypting/decrypting algorithms."""

    def encrypt(self,text,shift):
        """Encrypt using Ceaser Cypher algorithm.
        
        shift each character text by "shift" amount 1-26
        """
       
        result = ""
       
        # transverse the plain text
        for i in range(len(text)):
        
            char = text[i]
            
            # Encrypt uppercase characters in plain text
            if (char.isupper()) and (ord(char) > 65) and (ord(char) < 124):
            
                result += chr((ord(char) + shift-65) % 26 + 65)
                
                # Encrypt lowercase characters in plain text
            
            #add lower case letters
            elif (char.islower()) and (ord(char) > 65) and (ord(char) < 124):
            
                result += chr((ord(char) + shift - 97) % 26 + 97)
            
            else:
                #add symbols and numbers
                result += char
                
        return result
        
    def decrypt(self,text,shift):
        """Decrypt ceaser cipher algorithm."""
       
        result = ""
       
        # transverse the plain text
        for i in range(len(text)):
        
            char = text[i]
            
            # Encrypt uppercase characters in plain text

            if ((char.isupper()) and (ord(char) > 65) and (ord(char) < 124)):
            
                result += chr((ord(char) - shift- 65) % 26 + 65)
                
            # Encrypt lowercase characters in plain text
                
            elif(char.islower()) and (ord(char) > 65) and (ord(char) < 124):
            
                result += chr((ord(char) - shift - 97) % 26 + 97)
            
            else:
                #add symbols and numbers
                result += char
                
        return result
        
    def b64encode(self,ciphered_text):
        """For additional security encode the password using base64."""
        
        return base64.b64encode(ciphered_text.encode())
        
    def b64decode(self,ciphered_text):
        """For additional security decode the password using base64."""
        
        return base64.b64decode(ciphered_text).decode()
    

if __name__ =="__main__":

    cc = Encryption()
    
    #check the above function
    text = "bobby69@#"
    s = 3
    
    e1 = cc.encrypt(text,s)
    
    #convert ciphered text to byte string
    cipher = e1
    
    #encode byte string with base64 encoding
    encode = cc.b64encode(cipher)
    print(encode)

    #decode byte string with base 64 decoding and returns a string
    decode = cc.b64decode(encode)
    print(decode)

    original = cc.decrypt(decode,s)
    print(original)
