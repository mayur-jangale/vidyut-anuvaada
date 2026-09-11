# Sutra प.5.1.27: शतमानविंशतिकसहस्रवसनादण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatamAnaviMSatikasahasravasanAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.27"
SUTRA_TEXT = "शतमानविंशतिकसहस्रवसनादण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatamAnaviMSatikasahasravasanAdaR"


class Sutra5127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.27: अग्निः'),
		('रामः', '', 'प.5.1.27: रामः'),
		('सीता', '', 'प.5.1.27: सीता'),
	]

