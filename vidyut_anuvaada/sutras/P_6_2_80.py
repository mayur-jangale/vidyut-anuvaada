# Sutra प.6.2.80: उपमानं शब्दार्थप्रकृतावेव
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.80"
SUTRA_TEXT = "उपमानं शब्दार्थप्रकृतावेव"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6280:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.80: अग्निः'),
		('रामः', '', 'प.6.2.80: रामः'),
		('सीता', '', 'प.6.2.80: सीता'),
	]

