import math
from icecream import ic
ic('The age of {0} is {1}'.format('Jim', 23))
ic("The age of {0} is {1}, {0}'s birthday is on {2}".format('Fred', 24, 'October 32'))
ic("Reticulation spline {} of {}".format(4,23))
ic("Current position {latitude}  {longitude}".format(latitude='60N', longitude="5E"))
ic("galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=(62.2,22.1,00.5)))
ic("Math constants: pi={m.pi}, e={m.e}".format(m=math))
