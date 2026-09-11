# Sutra प.6.2.197: द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ
# (Sandhi (euphonic combination)) — dvitriByAM pAddanmUrDasu bahuvrIhO

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.197"
SUTRA_TEXT = "द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ"
SUTRA_DESC = "(Sandhi (euphonic combination)) — dvitriByAM pAddanmUrDasu bahuvrIhO"


class Sutra62197:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.197: अग्निः'),
		('रामः', '', 'प.6.2.197: रामः'),
		('सीता', '', 'प.6.2.197: सीता'),
	]

