# Sutra प.6.2.3: वर्णो वर्णेष्वनेते
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.3"
SUTRA_TEXT = "वर्णो वर्णेष्वनेते"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra623:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.3: अग्निः'),
		('रामः', '', 'प.6.2.3: रामः'),
		('सीता', '', 'प.6.2.3: सीता'),
	]

