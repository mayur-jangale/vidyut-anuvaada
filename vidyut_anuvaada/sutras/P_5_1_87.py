# Sutra प.5.1.87: रात्र्यहस्संवत्सराच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rAtryahassaMvatsarAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.87"
SUTRA_TEXT = "रात्र्यहस्संवत्सराच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rAtryahassaMvatsarAcca"


class Sutra5187:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.87: अग्निः'),
		('रामः', '', 'प.5.1.87: रामः'),
		('सीता', '', 'प.5.1.87: सीता'),
	]

