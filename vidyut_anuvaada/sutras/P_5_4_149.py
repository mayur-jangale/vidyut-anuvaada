# Sutra प.5.4.149: पूर्णाद्विभाषा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrRAdviBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.149"
SUTRA_TEXT = "पूर्णाद्विभाषा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrRAdviBAzA"


class Sutra54149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.149: अग्निः'),
		('रामः', '', 'प.5.4.149: रामः'),
		('सीता', '', 'प.5.4.149: सीता'),
	]

