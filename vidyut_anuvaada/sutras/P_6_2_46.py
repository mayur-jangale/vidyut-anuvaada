# Sutra प.6.2.46: कर्मधारयेऽनिष्ठा
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.46"
SUTRA_TEXT = "कर्मधारयेऽनिष्ठा"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.46: अग्निः'),
		('रामः', '', 'प.6.2.46: रामः'),
		('सीता', '', 'प.6.2.46: सीता'),
	]

