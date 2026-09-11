# Sutra प.1.1.33: प्रथमचरमतयाल्पार्धकतिपयनेमाश्च
# (Samjna (technical definitions)) — praTamacaramatayAlpArDakatipayanemASca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.33"
SUTRA_TEXT = "प्रथमचरमतयाल्पार्धकतिपयनेमाश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — praTamacaramatayAlpArDakatipayanemASca"


class Sutra1133:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_33
		return apply_1_1_33(word, pos)

	EXAMPLES = [
		('प्रथम', '', 'distance-token=yes:प्रथम'),
		('चरम', '', 'distance-token=yes:चरम'),
		('कतिपय', '', 'distance-token=yes:कतिपय'),
		('दश', '', 'distance-token=no:दश'),
	]

