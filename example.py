import hues
import random
import time


class ThisPlanetIsProtected(Exception):
  pass


def destroy_planet(planet):
  if planet == 'Earth':
    raise ThisPlanetIsProtected
  return random.randint(0, 100) < 42

if __name__ == '__main__':
  hues.info('Destroying the planets. Please wait.')

  for planet in ('Murcury', 'Venus', 'Earth', 'Mars', 'Uranus',):
    try:
      success = destroy_planet(planet)
    except ThisPlanetIsProtected:
      hues.warn('The Doctor saved', planet)
    else:
      if success:
        hues.success('Destroyed', planet)
      else:
        hues.error('Could not destroy', planet)
    time.sleep(.5)

  hues.info('So long, and thanks for all the fish.')
