# Sutra प.5.2.121: अस्मायामेधास्रजो विनिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — asmAyAmeDAsrajo viniH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.121"
SUTRA_TEXT = "अस्मायामेधास्रजो विनिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — asmAyAmeDAsrajo viniH"


class Sutra52121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.121: अग्निः'),
		('रामः', '', 'प.5.2.121: रामः'),
		('सीता', '', 'प.5.2.121: सीता'),
	]

