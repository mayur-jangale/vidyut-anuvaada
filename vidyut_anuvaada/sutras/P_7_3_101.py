# Sutra प.7.3.101: अतो दीर्घो यञि
# (Taddhita (secondary derivations)) — ato dIrGo yaYi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.101"
SUTRA_TEXT = "अतो दीर्घो यञि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ato dIrGo yaYi"


class Sutra73101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.101: अग्निः'),
		('रामः', '', 'प.7.3.101: रामः'),
		('सीता', '', 'प.7.3.101: सीता'),
	]

