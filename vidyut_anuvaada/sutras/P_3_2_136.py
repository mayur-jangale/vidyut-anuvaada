# Sutra प.3.2.136: अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — alaMkfYnirAkfYprajanotpacotpatonmadarucyapatrapavftuvfDusahacara izRuc

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.136"
SUTRA_TEXT = "अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — alaMkfYnirAkfYprajanotpacotpatonmadarucyapatrapavftuvfDusahacara izRuc"


class Sutra32136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

