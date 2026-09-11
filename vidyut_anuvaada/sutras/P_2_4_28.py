# Sutra प.2.4.28: हेमन्तशिशिरावहोरात्रे च च्छन्दसि
# (Samasa (compound formation)) — hemantaSiSirAvahorAtre ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.28"
SUTRA_TEXT = "हेमन्तशिशिरावहोरात्रे च च्छन्दसि"
SUTRA_DESC = "(Samasa (compound formation)) — hemantaSiSirAvahorAtre ca cCandasi"


class Sutra2428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

