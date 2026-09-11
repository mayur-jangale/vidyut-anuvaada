# Sutra प.2.3.4: अन्तराऽन्तरेण युक्ते
# (Samasa (compound formation)) — antarA'ntareRa yukte

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.4"
SUTRA_TEXT = "अन्तराऽन्तरेण युक्ते"
SUTRA_DESC = "(Samasa (compound formation)) — antarA'ntareRa yukte"


class Sutra234:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

