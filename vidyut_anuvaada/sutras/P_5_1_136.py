# Sutra प.5.1.136: ब्रह्मणस्त्वः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmaRastvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.136"
SUTRA_TEXT = "ब्रह्मणस्त्वः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — brahmaRastvaH"


class Sutra51136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.136: अग्निः'),
		('रामः', '', 'प.5.1.136: रामः'),
		('सीता', '', 'प.5.1.136: सीता'),
	]

