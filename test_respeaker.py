import speech_recognition as sr

print("started")

r = sr.Recognizer()
mic = sr.Microphone(device_index = 2)
print("adjusting")
with mic as source:
	r.adjust_for_ambient_noise(source, duration = 5)
	r.dynamic_energy_threshold = True	
			
while(1):
	with mic as source:
		try:
			print("listening")
			audio = r.listen(source)
			
			print("recognizing")
			transcript = r.recognize_google(audio)
			
			print(transcript)
		
		except Exception as e:
			print(e)
		
