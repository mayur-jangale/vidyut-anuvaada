# Sutra प.6.1.172: अष्टनो दीर्घात्
# sandhi-sūtra प.6.1.172

from P_6_1 import apply_6_1_172

SUTRA_CODE = "प.6.1.172"
SUTRA_TEXT = "अष्टनो दीर्घात्"
SUTRA_DESC = "sandhi-sūtra प.6.1.172"


class Sutra61172:
	def apply(self, word, pos):
		return apply_6_1_172(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.172:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.172:marker=padartha;input=रामः'),
		('सीता', '', '6.1.172:marker=padartha;input=सीता'),
	]
