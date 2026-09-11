# Sutra प.8.2.43: संयोगादेरातो धातोर्यण्वतः
# (Final transformations (tripāḍī)) — saMyogAderAto DAtoryaRvataH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.43"
SUTRA_TEXT = "संयोगादेरातो धातोर्यण्वतः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — saMyogAderAto DAtoryaRvataH"


class Sutra8243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.43: अग्निः'),
		('रामः', '', 'प.8.2.43: रामः'),
		('सीता', '', 'प.8.2.43: सीता'),
	]

