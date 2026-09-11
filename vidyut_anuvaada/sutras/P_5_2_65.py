# Sutra प.5.2.65: धनहिरण्यात् कामे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — DanahiraRyAt kAme

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.65"
SUTRA_TEXT = "धनहिरण्यात् कामे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — DanahiraRyAt kAme"


class Sutra5265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.65: अग्निः'),
		('रामः', '', 'प.5.2.65: रामः'),
		('सीता', '', 'प.5.2.65: सीता'),
	]

