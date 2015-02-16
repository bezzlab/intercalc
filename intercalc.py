# LC-MS Interferent Calculator
# Developed with Python 2.7.8

# parameters (hard coded for now)
targetfile     = "test/targets.tsv"
backgroundfile = "test/background.tsv"
massaccuracy   = 0.1
peakwidth      = 1

from background import *
from constants import *

print "\nCreating background object ..."

# create background object by reading interferent file
b = Background(backgroundfile, massaccuracy, peakwidth)

# open new file (to write results to)
outfile = open("intercalc.tsv", "w")  # output always called calcinter.tsv

# open target file (read only)
infile = open(targetfile, "r")

# append interferent probablity column heading
outfile.write(infile.readline().rstrip()+"\tInteferent probability\n")
print "Annotating targets with interference data "

# step through target peptides one by one and append calcualted interferent probability
for line in infile:
  # extract mass and hydrophobicity from line (could there be a one line way to do this?)
  splitline = line.split("\t")
  mass = float(splitline[MOLWEIGHT_COL])
  h = float(splitline[HYDRO_COL])
  # ask background object for peptide-specific interfrence information
  ptotal = b.interference(mass, h)
  # write peptide line with appended ptotal to new file
  outfile.write(line.rstrip() + "\t" + str(ptotal) + "\n")

infile.close()
outfile.close()

print b.massaccuracy

input("\nDone. Press the Enter key to exit.")
