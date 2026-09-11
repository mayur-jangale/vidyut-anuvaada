# Sutra प.6.2.177: उपसर्गात् स्वाङ्गं ध्रुवमपर्शु
# (Sandhi (euphonic combination)) — upasargAt svANgaM DruvamaparSu

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.177"
SUTRA_TEXT = "उपसर्गात् स्वाङ्गं ध्रुवमपर्शु"
SUTRA_DESC = "(Sandhi (euphonic combination)) — upasargAt svANgaM DruvamaparSu"


class Sutra62177:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.177: अग्निः'),
		('रामः', '', 'प.6.2.177: रामः'),
		('सीता', '', 'प.6.2.177: सीता'),
	]

