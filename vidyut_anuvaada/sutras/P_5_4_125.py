# Sutra प.5.4.125: जम्भा सुहरिततृणसोमेभ्यः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jamBA suharitatfRasomeByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.125"
SUTRA_TEXT = "जम्भा सुहरिततृणसोमेभ्यः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jamBA suharitatfRasomeByaH"


class Sutra54125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.125: अग्निः'),
		('रामः', '', 'प.5.4.125: रामः'),
		('सीता', '', 'प.5.4.125: सीता'),
	]

