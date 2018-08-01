from __future__ import print_function
import sys
from sets import Set

fi = sys.argv[1]
outputfilename = 'generated_map.dat'

# Build the id to fed map
idtofed_map = {}
mapping = open(fi)
for line in mapping:
  s = line.split()
  side = s[0]
  eta = s[1]
  phi = s[2]
  depth = s[3]
  fed = s[4]
  i = s[5]
  if len(s)==7:
    det = s[6]
  identifier = str(side)+","+str(eta)+","+str(phi)+","+str(depth)
  #identifier = str(i)
  if identifier in idtofed_map:
    idtofed_map[identifier].append(fed)
  else:
    idtofed_map[identifier] = []
    idtofed_map[identifier].append(fed)
  
# Build the id to detector map
idtodet_map = {}
mapping = open(fi)
for line in mapping:
  s = line.split()
  side = s[0]
  eta = s[1]
  phi = s[2]
  depth = s[3]
  fed = s[4]
  i = s[5]
  det = ''
  if len(s)==7:
    det = s[6]
  identifier = str(side)+","+str(eta)+","+str(phi)+","+str(depth)
  #identifier = str(i)
  if identifier in idtodet_map:
    idtodet_map[identifier].append(det)
  else:
    idtodet_map[identifier] = []
    idtodet_map[identifier].append(det)

# Build the fed to id map
fedtoid_map = {}
for idi in idtofed_map:
  feds = idtofed_map[idi]
  for fed in feds:
    if fed in fedtoid_map:
      fedtoid_map[fed].append(idi)
    else:
      fedtoid_map[fed] = []
      fedtoid_map[fed].append(idi)
  
# output results

print('\nJust ids with more than one FED:')
for entry in idtofed_map:
  feds = idtofed_map[entry]
  if not len(feds) == 1:
    print(entry.rjust(10), ": ", end='')
    for fed in feds:
      print(fed, end=' ')
    print()

print('\nJust the ids that map to different FEDs')
for entry in idtofed_map:
  list_feds = idtofed_map[entry]
  feds = Set(list_feds)
  if not len(feds) == 1:
    print(entry.rjust(10), ": ", end='')
    for fed in feds:
      print(fed, end=' ')
    print()

print('\nFor the ids that map to different FEDs, which detectors?')
for entry in idtofed_map:
  list_feds = idtofed_map[entry]
  feds = Set(list_feds)
  if not len(feds) == 1:
    print(entry.rjust(10), ": ", end='')
    print(Set(idtodet_map[entry]))

print('\nAll the feds and associated ids\n')
keys = fedtoid_map.keys()
keys.sort()
for fed in keys:
  print(fed, ": ", end=' ')
  ids = fedtoid_map[fed]
  ids.sort()
  for idi in Set(ids):
    print(idi, end='')
    dets = Set(idtodet_map[idi])
    if not len(dets)==1:
      print('<', end=' ')
    else:
      print('', end=' ')    
  print('\n')

print('\nAll the feds and associated ids\n')
keys = fedtoid_map.keys()
keys.sort()
for fed in keys:
  print(fed, ": ", end=' ')
  ids = fedtoid_map[fed]
  ids.sort()
  for idi in Set(ids):
    print(idi, end='')
    otherfeds = Set(idtofed_map[idi]) - Set([fed])
    if not len(otherfeds)==0:
      print('<'+str(otherfeds.pop()), end=' ')
    else:
      print('', end=' ')
  print('\n')

print()

# write mapping out to file
output = open(outputfilename, 'w')
for entry in idtofed_map:
  newline = ''
  feds = idtofed_map[entry]
  newline = newline+entry+' '
  for fed in feds:
    newline = newline+fed+','
  newline = newline[0:len(newline)-1]
  newline = newline+'\n'
  output.write(newline)

output.close()
