import bluetooth

nearby_devices = bluetooth.discover_devices()

print("herhe")
for bdaddr in nearby_devices:
    print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")

    
print("herhe")