# Sutra प.5.1.127: कपिज्ञात्योर्ढक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kapijYAtyorQak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.127"
SUTRA_TEXT = "कपिज्ञात्योर्ढक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kapijYAtyorQak"


class Sutra51127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.127: अग्निः'),
		('रामः', '', 'प.5.1.127: रामः'),
		('सीता', '', 'प.5.1.127: सीता'),
	]

