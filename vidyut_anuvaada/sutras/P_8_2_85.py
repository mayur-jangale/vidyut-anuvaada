# Sutra प.8.2.85: हैहेप्रयोगे हैहयोः
# (Final transformations (tripāḍī)) — hEheprayoge hEhayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.85"
SUTRA_TEXT = "हैहेप्रयोगे हैहयोः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — hEheprayoge hEhayoH"


class Sutra8285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.85: अग्निः'),
		('रामः', '', 'प.8.2.85: रामः'),
		('सीता', '', 'प.8.2.85: सीता'),
	]

