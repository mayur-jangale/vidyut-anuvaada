# Sutra प.5.1.25: कंसाट्टिठन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaMsAwwiWan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.25"
SUTRA_TEXT = "कंसाट्टिठन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kaMsAwwiWan"


class Sutra5125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.25: अग्निः'),
		('रामः', '', 'प.5.1.25: रामः'),
		('सीता', '', 'प.5.1.25: सीता'),
	]

