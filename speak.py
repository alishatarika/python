import win32com.client 
  
# Calling the Dispatch method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
list=["alisha","ankush","tanush"]
for i in list:
   l=speaker.speak(f"shoutout to {i}")
   
