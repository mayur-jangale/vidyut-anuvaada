# Sutra प.5.3.96: इवे प्रतिकृतौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ive pratikftO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.96"
SUTRA_TEXT = "इवे प्रतिकृतौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ive pratikftO"


class Sutra5396:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.96: अग्निः'),
		('रामः', '', 'प.5.3.96: रामः'),
		('सीता', '', 'प.5.3.96: सीता'),
	]

