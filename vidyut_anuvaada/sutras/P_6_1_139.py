# Sutra प.6.1.139: उपात् प्रतियत्नवैकृतवाक्याध्याहारेषु
# sandhi-sūtra प.6.1.139

from P_6_1 import apply_6_1_139

SUTRA_CODE = "प.6.1.139"
SUTRA_TEXT = "उपात् प्रतियत्नवैकृतवाक्याध्याहारेषु"
SUTRA_DESC = "sandhi-sūtra प.6.1.139"


class Sutra61139:
	def apply(self, word, pos):
		return apply_6_1_139(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.139:input=अग्निः'),
		('रामः', '', '6.1.139:input=रामः'),
		('सीता', '', '6.1.139:input=सीता'),
	]
