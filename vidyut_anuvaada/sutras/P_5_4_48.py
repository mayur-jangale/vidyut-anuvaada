# Sutra प.5.4.48: षष्ठ्या व्याश्रये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWyA vyASraye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.48"
SUTRA_TEXT = "षष्ठ्या व्याश्रये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazWyA vyASraye"


class Sutra5448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.48: अग्निः'),
		('रामः', '', 'प.5.4.48: रामः'),
		('सीता', '', 'प.5.4.48: सीता'),
	]

