# Sutra प.5.2.137: संज्ञायां मन्माभ्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM manmAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.137"
SUTRA_TEXT = "संज्ञायां मन्माभ्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM manmAByAm"


class Sutra52137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.137: अग्निः'),
		('रामः', '', 'प.5.2.137: रामः'),
		('सीता', '', 'प.5.2.137: सीता'),
	]

