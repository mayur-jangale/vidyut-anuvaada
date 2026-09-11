# Sutra प.5.1.73: संशयमापन्नः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMSayamApannaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.73"
SUTRA_TEXT = "संशयमापन्नः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saMSayamApannaH"


class Sutra5173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.73: अग्निः'),
		('रामः', '', 'प.5.1.73: रामः'),
		('सीता', '', 'प.5.1.73: सीता'),
	]

