# Sutra प.5.2.54: द्वेस्तीयः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvestIyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.54"
SUTRA_TEXT = "द्वेस्तीयः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvestIyaH"


class Sutra5254:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.54: अग्निः'),
		('रामः', '', 'प.5.2.54: रामः'),
		('सीता', '', 'प.5.2.54: सीता'),
	]

