from Auto import Auto

minu_uus_auto = auto("audi", "a6", 2017)

print(minu_uus_auto.kirjeldus())
minu_uus_auto.odomeeter()
minu_uus_auto.odomeetri_nait = (2)
minu_uus_auto.odomeeter()

minu_uus_auto.suurenda_odomeeter(30)
minu_uus_auto.odomeeter()