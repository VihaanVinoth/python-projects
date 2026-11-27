def compress_string(input_string: str) -> str: 
   if not input_string: 
       return "" 

   compressed = [] 

   count = 1 

   for i in range(1, len(input_string)): 
       if input_string[i] == input_string[i - 1]: 
           count += 1 
       else: 
           compressed.append(input_string[i - 1]) 
           if count > 1: 
               compressed.append(str(count)) 
           count = 1 

   compressed.append(input_string[-1]) 

   if count > 1: 
       compressed.append(str(count)) 

   return "".join(compressed) 

def decompress_string(compressed_string: str) -> str: 

   if not compressed_string: 
       return "" 

   decompressed = [] 

   i = 0 

   n = len(compressed_string) 

   while i < n: 
       char = compressed_string[i] 

       i += 1 

       num_start = i 

       while i < n and compressed_string[i].isdigit(): 
           i += 1 
       if i > num_start: 
           count = int(compressed_string[num_start:i]) 
           decompressed.append(char * count) 
       else: 
           decompressed.append(char) 
   return "".join(decompressed) 

print(compress_string("aaabbcccccaaa"))   
print(decompress_string("a3b2c5a3"))     
print(compress_string("a"))             
print(decompress_string("a"))         
print(compress_string("abcde"))           
print(decompress_string("abcde"))          
print(compress_string("aaabbbaaa"))        
print(decompress_string("a3b3a3"))         
print(compress_string("aaaaaaaaaaaa"))     
print(decompress_string("a12"))            

 
 

 
 

 