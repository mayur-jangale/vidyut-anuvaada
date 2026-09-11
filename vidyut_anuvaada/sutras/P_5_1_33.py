# Sutra प.5.1.33: खार्या ईकन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — KAryA Ikan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.33"
SUTRA_TEXT = "खार्या ईकन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — KAryA Ikan"


class Sutra5133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.33: अग्निः'),
		('रामः', '', 'प.5.1.33: रामः'),
		('सीता', '', 'प.5.1.33: सीता'),
	]

