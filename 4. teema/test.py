from Jaatisekiosk import Jaatisekiosk

kiosk = Jaatisekiosk("Vanilla", "jäätis")
kiosk.restoraani.kirjeldus()
kiosk.lisajaatisevalikusse("Vanilla")
kiosk.lisajaatisevalikusse("Maasika")
kiosk.naita_jaatise_valik()