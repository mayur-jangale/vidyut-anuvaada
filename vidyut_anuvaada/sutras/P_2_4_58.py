# Sutra प.2.4.58: ण्यक्षत्रियार्षञितो यूनि लुगणिञोः
# (Samasa (compound formation)) — RyakzatriyArzaYito yUni lugaRiYoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.58"
SUTRA_TEXT = "ण्यक्षत्रियार्षञितो यूनि लुगणिञोः"
SUTRA_DESC = "(Samasa (compound formation)) — RyakzatriyArzaYito yUni lugaRiYoH"


class Sutra2458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

