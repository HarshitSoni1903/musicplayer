import offlinecontrol

index=int(raw_input("enter a number"))

ob = offlinecontrol.monitorthread()
ob.start()

index=int(raw_input("enter a number"))