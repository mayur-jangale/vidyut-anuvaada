# Sutra प.5.2.107: ऊषसुषिमुष्कमधो रः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — UzasuzimuzkamaDo raH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.107"
SUTRA_TEXT = "ऊषसुषिमुष्कमधो रः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — UzasuzimuzkamaDo raH"


class Sutra52107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.107: अग्निः'),
		('रामः', '', 'प.5.2.107: रामः'),
		('सीता', '', 'प.5.2.107: सीता'),
	]

