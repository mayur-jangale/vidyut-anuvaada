# Sutra प.7.2.66: इडत्त्यर्तिव्ययतीनाम्
# (Taddhita (secondary derivations)) — iqattyartivyayatInAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.66"
SUTRA_TEXT = "इडत्त्यर्तिव्ययतीनाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — iqattyartivyayatInAm"


class Sutra7266:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.66: अग्निः'),
		('रामः', '', 'प.7.2.66: रामः'),
		('सीता', '', 'प.7.2.66: सीता'),
	]

