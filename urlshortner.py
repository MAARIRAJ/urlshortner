
import pyshorteners

url = input("Enter the URL: ")
print("New URL: ", pyshorteners.Shortener().tinyurl.short(url))
