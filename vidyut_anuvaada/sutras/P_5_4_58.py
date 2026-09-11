# Sutra प.5.4.58: कृञो द्वितीयतृतीयशम्बबीजात् कृषौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kfYo dvitIyatftIyaSambabIjAt kfzO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.58"
SUTRA_TEXT = "कृञो द्वितीयतृतीयशम्बबीजात् कृषौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kfYo dvitIyatftIyaSambabIjAt kfzO"


class Sutra5458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.58: अग्निः'),
		('रामः', '', 'प.5.4.58: रामः'),
		('सीता', '', 'प.5.4.58: सीता'),
	]

