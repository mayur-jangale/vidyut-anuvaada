# Sutra प.5.2.123: ऊर्णाया युस्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — UrRAyA yus

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.123"
SUTRA_TEXT = "ऊर्णाया युस्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — UrRAyA yus"


class Sutra52123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.123: अग्निः'),
		('रामः', '', 'प.5.2.123: रामः'),
		('सीता', '', 'प.5.2.123: सीता'),
	]

