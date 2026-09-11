# Sutra प.5.4.5: न सामिवचने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — na sAmivacane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.5"
SUTRA_TEXT = "न सामिवचने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — na sAmivacane"


class Sutra545:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.5: अग्निः'),
		('रामः', '', 'प.5.4.5: रामः'),
		('सीता', '', 'प.5.4.5: सीता'),
	]

