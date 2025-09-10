#import os

#print(os.getcwd())    # shows current working directory
#os.makedirs("test_folder", exist_ok=True)  # create folder
#print(os.listdir())   # lists files/folders in current dir

#import os

#os.makedirs("Fetched_Images", exist_ok=True)
#print("Current directory contents:", os.listdir()) #Checking if the folder has been formed

# Step 2: Ask user for an image URL
url = input("Enter the URL of the image you want to download: ")

print("You entered:", url)

