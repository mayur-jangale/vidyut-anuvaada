# Sutra प.5.4.130: ऊर्ध्वाद्विभाषा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — UrDvAdviBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.130"
SUTRA_TEXT = "ऊर्ध्वाद्विभाषा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — UrDvAdviBAzA"


class Sutra54130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.130: अग्निः'),
		('रामः', '', 'प.5.4.130: रामः'),
		('सीता', '', 'प.5.4.130: सीता'),
	]

