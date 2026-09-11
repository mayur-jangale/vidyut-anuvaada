# Sutra प.5.3.84: शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SevalasupariviSAlavaruRAryamAdInAM tftIyAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.84"
SUTRA_TEXT = "शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SevalasupariviSAlavaruRAryamAdInAM tftIyAt"


class Sutra5384:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.84: अग्निः'),
		('रामः', '', 'प.5.3.84: रामः'),
		('सीता', '', 'प.5.3.84: सीता'),
	]

