# Sutra प.5.4.106: द्वन्द्वाच्चुदषहान्तात् समाहारे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvAccudazahAntAt samAhAre

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.106"
SUTRA_TEXT = "द्वन्द्वाच्चुदषहान्तात् समाहारे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvAccudazahAntAt samAhAre"


class Sutra54106:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.106: अग्निः'),
		('रामः', '', 'प.5.4.106: रामः'),
		('सीता', '', 'प.5.4.106: सीता'),
	]

