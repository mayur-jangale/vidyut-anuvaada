# Sutra प.1.4.51: अकथितं च
# (Samjna (technical definitions)) — akaTitaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.51"
SUTRA_TEXT = "अकथितं च"
SUTRA_DESC = "(Samjna (technical definitions)) — akaTitaM ca"


class Sutra1451:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_51
		return apply_1_4_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'expressed-or-other:अग्निः'),
		('रामः', '', 'expressed-or-other:रामः'),
		('सीता', '', 'expressed-or-other:सीता'),
	]

