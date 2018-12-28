#Vers 1
def cannons_ready(gunners):
    return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'


#Vers 2
def cannons_ready(gunners):
    aye = sum(value == 'aye' for value in gunners.values())
    return 'Fire!' if aye == len(gunners) else 'Shiver me timbers!'