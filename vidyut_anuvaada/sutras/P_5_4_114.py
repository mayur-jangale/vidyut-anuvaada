# Sutra प.5.4.114: अङ्गुलेर्दारुणि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aNgulerdAruRi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.114"
SUTRA_TEXT = "अङ्गुलेर्दारुणि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aNgulerdAruRi"


class Sutra54114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.114: अग्निः'),
		('रामः', '', 'प.5.4.114: रामः'),
		('सीता', '', 'प.5.4.114: सीता'),
	]

