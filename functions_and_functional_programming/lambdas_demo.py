scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin',
              'Niels bohr', 'Dian fossey', 'Isaac Newton',
              'Grace Hopper', 'Charles Darwin', 'Lise Meitner' ]
sorted(scientists, key=lambda name: name.split()[-1])

last_name = lambda name: name.split()[-1]

