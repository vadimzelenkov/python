seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds - hours * 3600 - minutes * 60
print(hours, ":", minutes, ":", seconds)
