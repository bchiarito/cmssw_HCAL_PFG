import sys

#filename = sys.argv[1]
filename = 'detector_map.dat'

mapping = {}

data = open(filename, 'r')
for line in data:
  s = line.split()
  identifier = s[0]
  feds = s[1].split(',')
  mapping[identifier] = feds
    
def loc_to_fed(eta, phi, depth):
  side = eta / abs(eta)
  query = str(side)+','+str(abs(eta))+','+str(phi)+','+str(depth)
  try:
    return mapping[query]
  except KeyError, e:
    print "could not find", query
    return [0]
  except:
    raise

#print mapping

#user = ' '
#while not user == '':
#  user = str(raw_input('Enter coordinates (eta,phi,depth): '))
#  coords = user.split(',')
#  eta = int(coords[0])
#  phi = int(coords[1])
#  depth = int(coords[2])
#  print loc_to_fed(eta, phi, depth)
