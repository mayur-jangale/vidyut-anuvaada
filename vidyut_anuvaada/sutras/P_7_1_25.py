# Sutra प.7.1.25: अद्ड् डतरादिभ्यः पञ्चभ्यः
# (Taddhita (secondary derivations)) — adq qatarAdiByaH paYcaByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.25"
SUTRA_TEXT = "अद्ड् डतरादिभ्यः पञ्चभ्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — adq qatarAdiByaH paYcaByaH"


class Sutra7125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.25: अग्निः'),
		('रामः', '', 'प.7.1.25: रामः'),
		('सीता', '', 'प.7.1.25: सीता'),
	]

