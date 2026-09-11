# Sutra प.2.3.52: अधीगर्थदयेशां कर्मणि
# (Samasa (compound formation)) — aDIgarTadayeSAM karmaRi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.52"
SUTRA_TEXT = "अधीगर्थदयेशां कर्मणि"
SUTRA_DESC = "(Samasa (compound formation)) — aDIgarTadayeSAM karmaRi"


class Sutra2352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

