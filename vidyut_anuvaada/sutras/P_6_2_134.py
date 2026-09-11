# Sutra प.6.2.134: चूर्णादीन्यप्राणिषष्ठ्याः
# (Sandhi (euphonic combination)) — cUrRAdInyaprARizazWyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.134"
SUTRA_TEXT = "चूर्णादीन्यप्राणिषष्ठ्याः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — cUrRAdInyaprARizazWyAH"


class Sutra62134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.134: अग्निः'),
		('रामः', '', 'प.6.2.134: रामः'),
		('सीता', '', 'प.6.2.134: सीता'),
	]

