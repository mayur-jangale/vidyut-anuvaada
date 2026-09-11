# Sutra प.5.1.65: शीर्षच्छेदाद्यच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SIrzacCedAdyacca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.65"
SUTRA_TEXT = "शीर्षच्छेदाद्यच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SIrzacCedAdyacca"


class Sutra5165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.65: अग्निः'),
		('रामः', '', 'प.5.1.65: रामः'),
		('सीता', '', 'प.5.1.65: सीता'),
	]

