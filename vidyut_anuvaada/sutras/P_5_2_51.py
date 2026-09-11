# Sutra प.5.2.51: षट्कतिकतिपयचतुरां थुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zawkatikatipayacaturAM Tuk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.51"
SUTRA_TEXT = "षट्कतिकतिपयचतुरां थुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zawkatikatipayacaturAM Tuk"


class Sutra5251:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.51: अग्निः'),
		('रामः', '', 'प.5.2.51: रामः'),
		('सीता', '', 'प.5.2.51: सीता'),
	]

