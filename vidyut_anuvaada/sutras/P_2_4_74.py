# Sutra प.2.4.74: यङोऽचि च
# (Samasa (compound formation)) — yaNo'ci ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.74"
SUTRA_TEXT = "यङोऽचि च"
SUTRA_DESC = "(Samasa (compound formation)) — yaNo'ci ca"


class Sutra2474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

