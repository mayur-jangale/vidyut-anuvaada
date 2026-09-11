# Sutra प.5.4.45: अपादाने चाहीयरुहोः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — apAdAne cAhIyaruhoH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.45"
SUTRA_TEXT = "अपादाने चाहीयरुहोः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — apAdAne cAhIyaruhoH"


class Sutra5445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.45: अग्निः'),
		('रामः', '', 'प.5.4.45: रामः'),
		('सीता', '', 'प.5.4.45: सीता'),
	]

