# Sutra प.7.3.1: देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.1"
SUTRA_TEXT = "देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात्"
SUTRA_DESC = "taddhita — continued"


class Sutra731:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.1: अग्निः'),
		('रामः', '', 'प.7.3.1: रामः'),
		('सीता', '', 'प.7.3.1: सीता'),
	]

