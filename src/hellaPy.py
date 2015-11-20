from matplotlib import use, rcParams, cm
use('Agg')
import numpy, pylab

rcParams.update({
  'figure.autolayout'  : True,  
  'figure.figsize'     : (8,6),
  'figure.facecolor'   : [.75,.75,.75],
  'figure.edgecolor'   : [0,0,0],
  'figure.dpi'         : 100,
  'text.usetex'        : False,
  # Plot boundary properties
  'axes.linewidth'     : .5,
  'axes.edgecolor'     : [0,0,0,1],
  'axes.facecolor'     : [1,1,1,1],
  # Axes/Font spacing and size
  'font.size'          : 24,
  'axes.labelsize'     : 24,
  'axes.titlesize'     : 24,
  'xtick.major.pad'    : 8,
  'xtick.minor.pad'    : 8,
  'ytick.major.pad'    : 8,
  'ytick.minor.pad'    : 8,
  'legend.numpoints'   : 1,
  # Line and marker styles
  'lines.linewidth'       : 1,
  'lines.linestyle'       : '-',
  'lines.color'           : 'k',
  'lines.marker'          : None,
  'lines.markeredgewidth' : 1,
  'lines.markersize'      : 5,
  'lines.linewidth'       : 1,
  'lines.linewidth'       : 1,
  'lines.linewidth'       : 1,
  # Colormap
  'image.cmap'            : ['viridis', 'hot'],
  # Fonts
  'font.serif'         : [ 
      'Times New Roman',
      'Latin Modern Roman',
      'Computer Modern Roman',
      'Bitstream Vera Serif',
  ], 
  'font.sans-serif'    : [
      'Open Sans',
      'Computer Modern Sans',
      'Bitstream Vera Sans'
  ],
  'font.monospace'     : [
      'Anonymous Pro', 
      'Bitstream Vera Sans Mono'
  ],
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
    self.usetex     = False
    self.square     = (8,8)
    self.rectangle  = (8,6)
    self.figsize    = self.rectangle
    self.cmap       = 'viridis'
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

  def set_tex(self,boolean=False):
    self.usetex = boolean
    rcParams.update({
      'text.usetex' : self.usetex 
    })
    return None
  
  def set_figsize(self,figsize):
    self.figsize = figsize
    rcParams.update({
      'figure.figsize' : self.figsize  
    })
    return None

  def set_cmap(self,cmap):
    self.cmap = cmap
    rcParams.update({
      'image.cmap' : self.cmap
    })
    return None
# End Class

# Colors
yellow = numpy.array([1.0,1.0,0.0,0.8])
red    = numpy.array([1.0,0.0,0.0,0.8])
black  = numpy.array([0.0,0.0,0.0,1.0])
blue   = numpy.array([0.0,0.7,0.8,0.8])
teal   = numpy.array([0.0,0.8,0.6,0.8])
gray   = numpy.array([0.3,0.3,0.3,0.5])

dyellow = numpy.array([0.7,0.7,0.0,0.6])
dred    = numpy.array([0.7,0.0,0.0,0.6])

default_style = hellaPy('serif')

# axes style with auto layout and no labels
#re = [.1408,.128,.79,.8115]

def basic_plotting_help():
  print('                                                            \n\
data_array   = loadtxt(datafilename)                                 \n\
xdata, ydata = data_array[:,0], data_array[:,1]                      \n\
                                                                     \n\
figure(figsize=(l,w),dpi=r) # l,w are floats that represent inches   \n\
clf()                                                                \n\
plot(xdata,ydata,style)     # style default is "-b" (blue solid line)\n\
xlabel(x_string)                                                     \n\
ylabel(y_string)                                                     \n\
legend(array_of_strings)    # Does not have to be an array           \n\
title(title_string)                                                  \n\
savefig("fig.eps")                                                   \n\
  ')
  return None
