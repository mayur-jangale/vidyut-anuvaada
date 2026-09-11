# Sutra प.5.4.46: अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — atigrahAvyaTanakzepezvakartari tftIyAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.46"
SUTRA_TEXT = "अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — atigrahAvyaTanakzepezvakartari tftIyAyAH"


class Sutra5446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.46: अग्निः'),
		('रामः', '', 'प.5.4.46: रामः'),
		('सीता', '', 'प.5.4.46: सीता'),
	]

