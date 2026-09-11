# Sutra प.5.4.24: देवतान्तात्तादर्थ्ये यत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — devatAntAttAdarTye yat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.24"
SUTRA_TEXT = "देवतान्तात्तादर्थ्ये यत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — devatAntAttAdarTye yat"


class Sutra5424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.24: अग्निः'),
		('रामः', '', 'प.5.4.24: रामः'),
		('सीता', '', 'प.5.4.24: सीता'),
	]

