# Sutra प.1.4.81: छन्दसि परेऽपि
# (Samjna (technical definitions)) — Candasi pare'pi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.81"
SUTRA_TEXT = "छन्दसि परेऽपि"
SUTRA_DESC = "(Samjna (technical definitions)) — Candasi pare'pi"


class Sutra1481:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_81
		return apply_1_4_81(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-vedic-pare:अग्निः'),
		('रामः', '', 'not-vedic-pare:रामः'),
		('सीता', '', 'not-vedic-pare:सीता'),
	]

