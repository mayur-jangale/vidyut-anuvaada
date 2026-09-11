# Sutra प.6.2.38: महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.38"
SUTRA_TEXT = "महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.38: अग्निः'),
		('रामः', '', 'प.6.2.38: रामः'),
		('सीता', '', 'प.6.2.38: सीता'),
	]

