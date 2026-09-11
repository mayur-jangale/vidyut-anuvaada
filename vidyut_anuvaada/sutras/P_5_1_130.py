# Sutra प.5.1.130: हायनान्तयुवादिभ्योऽण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — hAyanAntayuvAdiByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.130"
SUTRA_TEXT = "हायनान्तयुवादिभ्योऽण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — hAyanAntayuvAdiByo'R"


class Sutra51130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.130: अग्निः'),
		('रामः', '', 'प.5.1.130: रामः'),
		('सीता', '', 'प.5.1.130: सीता'),
	]

