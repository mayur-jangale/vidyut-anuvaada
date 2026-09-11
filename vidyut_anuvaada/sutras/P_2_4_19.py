# Sutra प.2.4.19: तत्पुरुषोऽनञ् कर्मधारयः
# (Samasa (compound formation)) — tatpuruzo'naY karmaDArayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.19"
SUTRA_TEXT = "तत्पुरुषोऽनञ् कर्मधारयः"
SUTRA_DESC = "(Samasa (compound formation)) — tatpuruzo'naY karmaDArayaH"


class Sutra2419:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

