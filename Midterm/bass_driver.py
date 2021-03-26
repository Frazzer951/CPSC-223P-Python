from bass import Bass
from double_bass import Double_Bass

""" Test code used to test Bass and Double Bass classes 
    Do not change this code """
my_generic_bass = Bass("electric", "2019", "Fender Inc.")
print(my_generic_bass.get_bass_description())

my_classical_bass = Double_Bass("no", "2007", "Gyrogi Bananyai", "German", "C")
print(my_classical_bass.get_bass_description())

my_jazz_bass = Double_Bass("no", "2018", "Christopher Manuf.", "French")
print(my_jazz_bass.get_bass_description())

print(f'Jazz bass has a {my_jazz_bass.get_bow_type()} bow and Classical \
bass has a {my_classical_bass.get_bow_type()} bow.')
