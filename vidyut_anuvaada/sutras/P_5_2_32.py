# Sutra प.5.2.32: नेर्बिडज्बिरीसचौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — nerbiqajbirIsacO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.32"
SUTRA_TEXT = "नेर्बिडज्बिरीसचौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — nerbiqajbirIsacO"


class Sutra5232:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.32: अग्निः'),
		('रामः', '', 'प.5.2.32: रामः'),
		('सीता', '', 'प.5.2.32: सीता'),
	]

