# Sutra प.5.2.72: शीतोष्णाभ्यां कारिणि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SItozRAByAM kAriRi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.72"
SUTRA_TEXT = "शीतोष्णाभ्यां कारिणि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SItozRAByAM kAriRi"


class Sutra5272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.72: अग्निः'),
		('रामः', '', 'प.5.2.72: रामः'),
		('सीता', '', 'प.5.2.72: सीता'),
	]

