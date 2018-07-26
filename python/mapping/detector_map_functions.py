import sys

filename = sys.argv[1]

mapping = {}

data = open(filename, 'r')
for line in data:
  s = line.split()
  identifier = s[0]
  feds = s[1].split(',')
  mapping[identifier] = feds
    
def loc_to_fed(e, p, d):
  side = eta / abs(eta)
  return mapping[str(side)+','+str(abs(eta))+','+str(phi)+','+str(depth)]

print mapping

user = ' '
while not user == '':
  user = str(raw_input('Enter coordinates (eta,phi,depth): '))
  coords = user.split(',')
  eta = int(coords[0])
  phi = int(coords[1])
  depth = int(coords[2])
  print loc_to_fed(eta, phi, depth)
