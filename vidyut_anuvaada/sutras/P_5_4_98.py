# Sutra प.5.4.98: उत्तरमृगपूर्वाच्च सक्थ्नः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttaramfgapUrvAcca sakTnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.98"
SUTRA_TEXT = "उत्तरमृगपूर्वाच्च सक्थ्नः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uttaramfgapUrvAcca sakTnaH"


class Sutra5498:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.98: अग्निः'),
		('रामः', '', 'प.5.4.98: रामः'),
		('सीता', '', 'प.5.4.98: सीता'),
	]

