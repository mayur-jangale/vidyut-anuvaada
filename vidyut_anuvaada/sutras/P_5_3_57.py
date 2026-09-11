# Sutra प.5.3.57: द्विवचनविभज्योपपदे तरबीयसुनौ
# īyas, iṣṭha — comparative/superlative (different endings)

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.57"
SUTRA_TEXT = "द्विवचनविभज्योपपदे तरबीयसुनौ"
SUTRA_DESC = "īyas, iṣṭha — comparative/superlative (different endings)"


class Sutra5357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.57: अग्निः'),
		('रामः', '', 'प.5.3.57: रामः'),
		('सीता', '', 'प.5.3.57: सीता'),
	]

