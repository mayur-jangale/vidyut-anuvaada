# Sutra प.7.1.70: उगिदचां सर्वनामस्थानेऽधातोः
# (Taddhita (secondary derivations)) — ugidacAM sarvanAmasTAne'DAtoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.70"
SUTRA_TEXT = "उगिदचां सर्वनामस्थानेऽधातोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ugidacAM sarvanAmasTAne'DAtoH"


class Sutra7170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.70: अग्निः'),
		('रामः', '', 'प.7.1.70: रामः'),
		('सीता', '', 'प.7.1.70: सीता'),
	]

