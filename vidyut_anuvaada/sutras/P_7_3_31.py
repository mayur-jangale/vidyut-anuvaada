# Sutra प.7.3.31: यथातथयथापुरयोः पर्यायेण
# (Taddhita (secondary derivations)) — yaTAtaTayaTApurayoH paryAyeRa

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.31"
SUTRA_TEXT = "यथातथयथापुरयोः पर्यायेण"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yaTAtaTayaTApurayoH paryAyeRa"


class Sutra7331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.31: अग्निः'),
		('रामः', '', 'प.7.3.31: रामः'),
		('सीता', '', 'प.7.3.31: सीता'),
	]

