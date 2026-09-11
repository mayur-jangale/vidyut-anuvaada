# Sutra प.1.4.57: चादयोऽसत्त्वे
# (Samjna (technical definitions)) — cAdayo'sattve

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.57"
SUTRA_TEXT = "चादयोऽसत्त्वे"
SUTRA_DESC = "(Samjna (technical definitions)) — cAdayo'sattve"


class Sutra1457:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_57
		return apply_1_4_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-cAdi:अग्निः'),
		('रामः', '', 'not-cAdi:रामः'),
		('सीता', '', 'not-cAdi:सीता'),
	]

