import time

# def usingtheforloop():
#     for i in range(1,5+1):
#         print(i)


# inti = time.time()
# usingtheforloop()
# t1 = time.time()
# elapsed_time = t1 - inti
# print(elapsed_time)





# def usingthewhilelloop():
#    i=1
#    while i<=5:
#        print(i)
#        i+=1


# inti = time.time()
# usingthewhilelloop()
# t1 = time.time()
# elapsed_time = t1 - inti
# print(elapsed_time)




# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("How are you?")
# print("How are you?")
# time.sleep(3)
# speaker.Speak("I am fine bro")
# print("I am fine bro")



t=time.localtime()
print(t)


formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time) 


from datetime import datetime

# Custom format: "Weekday, Month Day, Year"
formatted = datetime.now().strftime("%A, %B %d, %Y")
print(formatted)  # Example: "Saturday, September 20, 2025"
