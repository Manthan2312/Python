# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello! I am speaking from Python using Windows text to speech.")
# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# # List available voices
# for voice in speaker.GetVoices():
#     print(voice.GetDescription())

# # Set a different voice
# speaker.Voice = speaker.GetVoices().Item(1)  # choose index from printed list
# speaker.Speak("This is a different voice.")



import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Rate = -10     # speed (-10 to +10)
speaker.Volume = 100  # volume (0 to 100)

speaker.Speak("I am speaking faster and a bit quieter now.")

