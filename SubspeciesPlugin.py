import sys

class SubspeciesPlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outfile = open(filename, 'w')
        for line in self.infile:
          if "subsp." in line or "bv." in line or "pv." in line or "serovar" in line or "Buchnera aphidicola" in line:
             outfile.write(line)
