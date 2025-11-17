# # number=(int)(input("Enter the Number to check"))
# # if number%2==0:
# #     print("even")
# # else:
# #     print("odd")




# # number=5
# # facto=1
# # for i in range(1,number+1):
# #     facto*=i

# # print(facto)


# # 1,1,2,3,5,8,13,21

# # str_e="Hello"

# # print(str_e[4])


# # str_r="My name is Manthan"
# # str_r=str_r.split()
# # print(str_r)


# listofnumber=[23,35,242,11,56]

# # print(max(listofnumber))
# # print(min(listofnumber))

# listofnumber_1=reversed(listofnumber)
# print(list(listofnumber_1))


import requests
import os
# image = requests.get(url="https://images.pexels.com/photos/1183099/pexels-photo-1183099.jpeg", stream=True)

# if image.status_code == 200:
# 	with open("downloaded_image.jpg", "wb") as f:
# 		f.write(image.content)
		
# else:
# 	print(f"Failed to download image: {image.status_code}")

# print(image)


# def func():

#     for i in range(5):
#         image = requests.get(url="https://picsum.photos/2000/3000")
#         if image.status_code == 200:
#             with open(f"file{i}.jpg", "wb") as f:
#                 f.write(image.content)
#             print(f"Saved file{i}.jpg")
#         else:
#             print(f"Failed to download image for file{i}.jpg: {image.status_code}")

# func()


# def fundelete():
#     for i in range(5):
#         os.remove(f"file{i}.jpg")
#         print("done")

# fundelete()
        

def func1():

   
        image = requests.get(url="https://youtu.be/nTbA7qrEsP0?si=iCXN6UgzsjWEgqjW")
        if image.status_code == 200:
            with open("file.mp4", "wb") as f:
                f.write(image.content)
            print(f"Saved video")
        else:
            print(f"Failed to download image for file: {image.status_code}")

func1()