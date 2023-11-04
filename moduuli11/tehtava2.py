from sahkoauto import Sahkoauto
from polttomoottoriauto import Polttomoottoriauto

sahkokaara = Sahkoauto('ABC-15', 180, 52.5)
icekaara = Polttomoottoriauto('ACD-123', 165, 32.3)

sahkokaara.kiihdyta(50)
sahkokaara.kulje(3)
sahkokaara.testi()

icekaara.kiihdyta(60)
icekaara.kulje(3)
icekaara.testi()