# Sutra प.7.3.37: शाच्छासाह्वाव्यावेपां युक्
# (Taddhita (secondary derivations)) — SAcCAsAhvAvyAvepAM yuk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.37"
SUTRA_TEXT = "शाच्छासाह्वाव्यावेपां युक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — SAcCAsAhvAvyAvepAM yuk"


class Sutra7337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.37: अग्निः'),
		('रामः', '', 'प.7.3.37: रामः'),
		('सीता', '', 'प.7.3.37: सीता'),
	]

