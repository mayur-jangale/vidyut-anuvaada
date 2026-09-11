# Sutra प.8.2.58: वित्तो भोगप्रत्यययोः
# (Final transformations (tripāḍī)) — vitto BogapratyayayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.58"
SUTRA_TEXT = "वित्तो भोगप्रत्यययोः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — vitto BogapratyayayoH"


class Sutra8258:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.58: अग्निः'),
		('रामः', '', 'प.8.2.58: रामः'),
		('सीता', '', 'प.8.2.58: सीता'),
	]

