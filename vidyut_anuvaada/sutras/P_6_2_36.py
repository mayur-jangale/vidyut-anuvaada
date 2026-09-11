# Sutra प.6.2.36: आचार्योपसर्जनश्चान्तेवासी
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.36"
SUTRA_TEXT = "आचार्योपसर्जनश्चान्तेवासी"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.36: अग्निः'),
		('रामः', '', 'प.6.2.36: रामः'),
		('सीता', '', 'प.6.2.36: सीता'),
	]

