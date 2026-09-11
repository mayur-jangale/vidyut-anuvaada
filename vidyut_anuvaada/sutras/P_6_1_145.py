# Sutra प.6.1.145: गोष्पदं सेवितासेवितप्रमाणेषु
# sandhi-sūtra प.6.1.145

from P_6_1 import apply_6_1_145

SUTRA_CODE = "प.6.1.145"
SUTRA_TEXT = "गोष्पदं सेवितासेवितप्रमाणेषु"
SUTRA_DESC = "sandhi-sūtra प.6.1.145"


class Sutra61145:
	def apply(self, word, pos):
		return apply_6_1_145(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.145:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.145:marker=padartha;input=रामः'),
		('सीता', '', '6.1.145:marker=padartha;input=सीता'),
	]
