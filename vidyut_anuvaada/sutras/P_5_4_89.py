# Sutra प.5.4.89: न संख्यादेः समाहारे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — na saMKyAdeH samAhAre

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.89"
SUTRA_TEXT = "न संख्यादेः समाहारे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — na saMKyAdeH samAhAre"


class Sutra5489:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.89: अग्निः'),
		('रामः', '', 'प.5.4.89: रामः'),
		('सीता', '', 'प.5.4.89: सीता'),
	]

