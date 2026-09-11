# Sutra प.4.2.3: नक्षत्रेण युक्तः कालः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatreRa yuktaH kAlaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.3"
SUTRA_TEXT = "नक्षत्रेण युक्तः कालः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatreRa yuktaH kAlaH"


class Sutra423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.3: अग्निः'),
		('रामः', '', 'प.4.2.3: रामः'),
		('सीता', '', 'प.4.2.3: सीता'),
	]

