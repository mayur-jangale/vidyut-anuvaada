# Sutra प.5.2.135: पुष्करादिभ्यो देशे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — puzkarAdiByo deSe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.135"
SUTRA_TEXT = "पुष्करादिभ्यो देशे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — puzkarAdiByo deSe"


class Sutra52135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.135: अग्निः'),
		('रामः', '', 'प.5.2.135: रामः'),
		('सीता', '', 'प.5.2.135: सीता'),
	]

