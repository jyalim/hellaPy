from matplotlib import use, rcParams
use('Agg')
import numpy, pylab

rcParams.update({
  'figure.autolayout'  : True,  
  'font.size'          : 24,
  'font.serif'         : ['Latin Modern Roman','Computer Modern Roman'], 
  'font.sans-serif'    : ['Open Sans','Computer Modern Sans'],
  'font.monospace'     : ['Anonymous Pro', 'Bitstream Vera Sans Mono'],
  'legend.numpoints'   : 1,
  'axes.labelsize'     : 24,
  'axes.titlesize'     : 24,
  'xtick.major.pad'    : 8,
  'xtick.minor.pad'    : 8,
  'ytick.major.pad'    : 8,
  'ytick.minor.pad'    : 8,
  'text.usetex'        : True,
})

class ColorBasis:
  # Default Colors
  r = numpy.array([ 1.,0.,0.,0. ])
  g = numpy.array([ 0.,1.,0.,0. ])
  b = numpy.array([ 0.,0.,1.,0. ])
  a = numpy.array([ 0.,0.,0.,1. ])
  # Initial Call
  def __init__(self, red=r,green=g,blue=b,alpha=a ):
    self.r    = red    # red
    self.g    = green  # green
    self.b    = blue   # blue
    self.a    = alpha  # alpha
    self.rgba = numpy.vstack([ red, green, blue, alpha ])
    return None

  def dot(self,choice):
    return numpy.dot(self.rgba,choice)

class hellaPy:
  def __init__(self,*args):
    self.fontfamily = 'serif'
    for arg in args:
      if arg == 'sans':
        self.fontfamily = 'sans-serif'
    rcParams.update({
      'font.family' : self.fontfamily,  
    }) 
    return None

  def set_fontfamily(self,family):
    self.fontfamily = family
    rcParams.update({
      'font.family' : self.fontfamily,
    })
    return None


# Colors
yellow = numpy.array([1.0,1.0,0.0,0.8])
red    = numpy.array([1.0,0.0,0.0,0.8])
black  = numpy.array([0.0,0.0,0.0,0.0])
blue   = numpy.array([0.0,0.7,0.8,0.8])
teal   = numpy.array([0.0,0.8,0.6,0.8])
gray   = numpy.array([0.3,0.3,0.3,0.5])

dyellow = numpy.array([0.6,0.6,0.0,0.6])
dred    = numpy.array([0.6,0.0,0.0,0.6])

font_style = hellaPy('serif')
