# Sutra प.5.4.116: अप् पूरणीप्रमाण्योः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ap pUraRIpramARyoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.116"
SUTRA_TEXT = "अप् पूरणीप्रमाण्योः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ap pUraRIpramARyoH"


class Sutra54116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.116: अग्निः'),
		('रामः', '', 'प.5.4.116: रामः'),
		('सीता', '', 'प.5.4.116: सीता'),
	]

