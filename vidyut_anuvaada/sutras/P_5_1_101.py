# Sutra प.5.1.101: तस्मै प्रभवति संतापादिभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasmE praBavati saMtApAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.101"
SUTRA_TEXT = "तस्मै प्रभवति संतापादिभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tasmE praBavati saMtApAdiByaH"


class Sutra51101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.101: अग्निः'),
		('रामः', '', 'प.5.1.101: रामः'),
		('सीता', '', 'प.5.1.101: सीता'),
	]

