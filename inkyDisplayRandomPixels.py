#!/usr/bin/python
'''
This program displays, on the console, the proportion of the White, Black, and Red randomized pixels on the inky display.
'''

from random import choice, randint
from inky.auto import auto
import PIL
import sys
import inky

'''
The ColorWeightInts dict establishes the color and a min/max bound.
The values for max don't matter in distribution, but the variance between the maxima does.
'''
ColorWeightInts = \
{
	'Example': [ 'min', 'max'],
	'White':   [ 1, 10**1 ],
	'Black':   [ 1, 10**1 ],
	'Red':     [ 1, 10**1 ]
}

'''
EXAMPLE = [
	inky.COLOR,
	randint(
		ColorWeightInts['Example'][0],
		ColorWeightInts['Example'][1]
		),
	'👾',
	'White',
	-1
	]
'''
WHITE	= [ inky.WHITE, randint(ColorWeightInts['White'][0], ColorWeightInts['White'][1]), '⬜️', 'White', -1 ]
BLACK	= [ inky.BLACK, randint(ColorWeightInts['Black'][0], ColorWeightInts['Black'][1]), '⬛️', 'Black', -1 ]
RED		= [ inky.RED,   randint(ColorWeightInts['Red'][0],   ColorWeightInts['Red'][1]),   '🟥', 'Red',   -1 ]

# Calculate the number of symbols to print in the color bar.
Total		= ( WHITE[1] + BLACK[1] + RED[1] ) / 100
WHITE[4]	= int(WHITE[1] // Total)
BLACK[4]	= int(BLACK[1] // Total)
RED[4]		= int(RED[1] // Total)

WeightedCols = []

def main():
	display = auto()

	for eachColor in WHITE, BLACK, RED:
		for eachWeight in range(eachColor[1]):
			WeightedCols.append(eachColor[0])
		# print(f"{eachColor[3] + ':':<8}{eachColor[2] * eachColor[1]}") # Proportions of the color.

	# For each color, print the symbol n times
	print(f"Levels: {WHITE[2] * WHITE[4]}{BLACK[2] * BLACK[4]}{RED[2] * RED[4]}")

	for x in range(display.width):
		for y in range(display.height):
			display.set_pixel(x, y, choice(WeightedCols))

	display.show()

if __name__ == '__main__':
	main()

