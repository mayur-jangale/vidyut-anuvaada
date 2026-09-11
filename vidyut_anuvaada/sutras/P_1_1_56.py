# Sutra प.1.1.56: स्थानिवदादेशोऽनल्विधौ
# (Samjna (technical definitions)) — sTAnivadAdeSo'nalviDO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.56"
SUTRA_TEXT = "स्थानिवदादेशोऽनल्विधौ"
SUTRA_DESC = "(Samjna (technical definitions)) — sTAnivadAdeSo'nalviDO"


class Sutra1156:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_56
		return apply_1_1_56(word, pos)

	EXAMPLES = [
		('स्थानिवत्', '', "प.1.1.56:sthānivadādeśo'nalviDHau;input=स्थानिवत्"),
		('अग्नि', '', "प.1.1.56:sthānivadādeśo'nalviDHau;input=अग्नि"),
	]

