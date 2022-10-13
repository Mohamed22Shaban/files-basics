import webbrowser    # => web without html language
import sys # => to run this code by cmd argument in windwos 
if len(sys.argv) > 1 :
    address = ' '.join(sys.argv[1:])  #=> use join to return address in string 
    
else:
    print('please entre the address')

webbrowser.open('https://www.google.com/maps/place/'+ address)