# Sutra प.1.4.2: विप्रतिषेधे परं कार्यम्
# vipratiṣedhe paraṃ kāryam — when two rules conflict, the later one wins

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.2"
SUTRA_TEXT = "विप्रतिषेधे परं कार्यम्"
SUTRA_DESC = "vipratiṣedhe paraṃ kāryam — when two rules conflict, the later one wins"


class Sutra142:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_2
		return apply_1_4_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-conflict:अग्निः'),
		('रामः', '', 'no-conflict:रामः'),
		('सीता', '', 'no-conflict:सीता'),
	]

