# Sutra प.5.4.39: मृदस्तिकन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — mfdastikan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.39"
SUTRA_TEXT = "मृदस्तिकन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — mfdastikan"


class Sutra5439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.39: अग्निः'),
		('रामः', '', 'प.5.4.39: रामः'),
		('सीता', '', 'प.5.4.39: सीता'),
	]

