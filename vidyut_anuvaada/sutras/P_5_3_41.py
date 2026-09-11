# Sutra प.5.3.41: विभाषावरस्य
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzAvarasya

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.41"
SUTRA_TEXT = "विभाषावरस्य"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzAvarasya"


class Sutra5341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.41: अग्निः'),
		('रामः', '', 'प.5.3.41: रामः'),
		('सीता', '', 'प.5.3.41: सीता'),
	]

