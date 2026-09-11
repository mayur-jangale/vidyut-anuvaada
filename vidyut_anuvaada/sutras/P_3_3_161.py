# Sutra प.3.3.161: विधिनिमन्त्रणामन्त्रणाधीष्टसंप्रश्नप्रार्थनेषु लिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viDinimantraRAmantraRADIzwasaMpraSnaprArTanezu liN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.161"
SUTRA_TEXT = "विधिनिमन्त्रणामन्त्रणाधीष्टसंप्रश्नप्रार्थनेषु लिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viDinimantraRAmantraRADIzwasaMpraSnaprArTanezu liN"


class Sutra33161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

