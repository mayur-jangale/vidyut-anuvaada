# Sutra प.6.2.121: कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे
# (Sandhi (euphonic combination)) — kUlatIratUlamUlaSAlA'kzasamamavyayIBAve

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.121"
SUTRA_TEXT = "कूलतीरतूलमूलशालाऽक्षसममव्ययीभावे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kUlatIratUlamUlaSAlA'kzasamamavyayIBAve"


class Sutra62121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.121: अग्निः'),
		('रामः', '', 'प.6.2.121: रामः'),
		('सीता', '', 'प.6.2.121: सीता'),
	]

