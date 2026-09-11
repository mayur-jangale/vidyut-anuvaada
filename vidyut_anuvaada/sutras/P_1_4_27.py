# Sutra प.1.4.27: वारणार्थानामीप्सितः
# (Samjna (technical definitions)) — vAraRArTAnAmIpsitaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.27"
SUTRA_TEXT = "वारणार्थानामीप्सितः"
SUTRA_DESC = "(Samjna (technical definitions)) — vAraRArTAnAmIpsitaH"


class Sutra1427:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_27
		return apply_1_4_27(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-apadana-vAraNa:अग्निः'),
		('रामः', '', 'not-apadana-vAraNa:रामः'),
		('सीता', '', 'not-apadana-vAraNa:सीता'),
	]

