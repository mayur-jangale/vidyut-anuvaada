# Sutra प.3.3.69: समुदोरजः पशुषु
# kṛtsamāsa — kṛdanta compounds

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.69"
SUTRA_TEXT = "समुदोरजः पशुषु"
SUTRA_DESC = "kṛtsamāsa — kṛdanta compounds"


class Sutra3369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

