# Sutra प.5.3.75: संज्ञायां कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.75"
SUTRA_TEXT = "संज्ञायां कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMjYAyAM kan"


class Sutra5375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.75: अग्निः'),
		('रामः', '', 'प.5.3.75: रामः'),
		('सीता', '', 'प.5.3.75: सीता'),
	]

