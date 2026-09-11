# Sutra प.2.4.56: अजेर्व्यघञपोः
# (Samasa (compound formation)) — ajervyaGaYapoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.56"
SUTRA_TEXT = "अजेर्व्यघञपोः"
SUTRA_DESC = "(Samasa (compound formation)) — ajervyaGaYapoH"


class Sutra2456:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

