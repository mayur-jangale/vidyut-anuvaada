# Sutra प.5.4.74: ऋक्पूरब्धूःपथामानक्षे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — fkpUrabDUHpaTAmAnakze

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.74"
SUTRA_TEXT = "ऋक्पूरब्धूःपथामानक्षे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — fkpUrabDUHpaTAmAnakze"


class Sutra5474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.74: अग्निः'),
		('रामः', '', 'प.5.4.74: रामः'),
		('सीता', '', 'प.5.4.74: सीता'),
	]

