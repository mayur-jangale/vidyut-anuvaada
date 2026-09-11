# Sutra प.5.3.66: प्रशंसायां रूपप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — praSaMsAyAM rUpap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.66"
SUTRA_TEXT = "प्रशंसायां रूपप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — praSaMsAyAM rUpap"


class Sutra5366:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.66: अग्निः'),
		('रामः', '', 'प.5.3.66: रामः'),
		('सीता', '', 'प.5.3.66: सीता'),
	]

