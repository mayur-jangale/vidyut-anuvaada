# Sutra प.5.3.95: अवक्षेपणे कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avakzepaRe kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.95"
SUTRA_TEXT = "अवक्षेपणे कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avakzepaRe kan"


class Sutra5395:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.95: अग्निः'),
		('रामः', '', 'प.5.3.95: रामः'),
		('सीता', '', 'प.5.3.95: सीता'),
	]

