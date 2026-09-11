# Sutra प.5.3.34: उत्तराधरदक्षिणादातिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarADaradakziRAdAtiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.34"
SUTRA_TEXT = "उत्तराधरदक्षिणादातिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttarADaradakziRAdAtiH"


class Sutra5334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.34: अग्निः'),
		('रामः', '', 'प.5.3.34: रामः'),
		('सीता', '', 'प.5.3.34: सीता'),
	]

