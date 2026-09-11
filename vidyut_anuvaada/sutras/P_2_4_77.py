# Sutra प.2.4.77: गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु
# (Samasa (compound formation)) — gAtisTAGupABUByaH sicaH parasmEpadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.77"
SUTRA_TEXT = "गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु"
SUTRA_DESC = "(Samasa (compound formation)) — gAtisTAGupABUByaH sicaH parasmEpadezu"


class Sutra2477:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

