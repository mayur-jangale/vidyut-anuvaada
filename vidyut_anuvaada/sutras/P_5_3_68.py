# Sutra प.5.3.68: विभाषा सुपो बहुच् पुरस्तात्तु
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA supo bahuc purastAttu

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.68"
SUTRA_TEXT = "विभाषा सुपो बहुच् पुरस्तात्तु"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA supo bahuc purastAttu"


class Sutra5368:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.68: अग्निः'),
		('रामः', '', 'प.5.3.68: रामः'),
		('सीता', '', 'प.5.3.68: सीता'),
	]

