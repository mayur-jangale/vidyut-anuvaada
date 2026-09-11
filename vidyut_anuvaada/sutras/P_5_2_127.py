# Sutra प.5.2.127: अर्शआदिभ्योऽच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — arSaAdiByo'c

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.127"
SUTRA_TEXT = "अर्शआदिभ्योऽच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — arSaAdiByo'c"


class Sutra52127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.127: अग्निः'),
		('रामः', '', 'प.5.2.127: रामः'),
		('सीता', '', 'प.5.2.127: सीता'),
	]

