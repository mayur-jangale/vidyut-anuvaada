# Sutra प.3.3.145: अनवकॢप्त्यमर्षयोरकिंवृत्तेऽपि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anavakxptyamarzayorakiMvftte'pi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.145"
SUTRA_TEXT = "अनवकॢप्त्यमर्षयोरकिंवृत्तेऽपि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anavakxptyamarzayorakiMvftte'pi"


class Sutra33145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

