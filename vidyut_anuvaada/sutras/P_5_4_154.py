# Sutra प.5.4.154: शेषाद्विभाषा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SezAdviBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.154"
SUTRA_TEXT = "शेषाद्विभाषा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SezAdviBAzA"


class Sutra54154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.154: अग्निः'),
		('रामः', '', 'प.5.4.154: रामः'),
		('सीता', '', 'प.5.4.154: सीता'),
	]

