# Sutra प.5.4.4: अनत्यन्तगतौ क्तात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anatyantagatO ktAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.4"
SUTRA_TEXT = "अनत्यन्तगतौ क्तात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anatyantagatO ktAt"


class Sutra544:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.4: अग्निः'),
		('रामः', '', 'प.5.4.4: रामः'),
		('सीता', '', 'प.5.4.4: सीता'),
	]

