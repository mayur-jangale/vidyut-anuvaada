# Sutra प.6.2.11: सदृशप्रतिरूपयोः सादृश्ये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.11"
SUTRA_TEXT = "सदृशप्रतिरूपयोः सादृश्ये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.11: अग्निः'),
		('रामः', '', 'प.6.2.11: रामः'),
		('सीता', '', 'प.6.2.11: सीता'),
	]

