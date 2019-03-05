import chimera
from chimera import openModels, Molecule
from chimera.colorTable import getColorByName

def colorBB():

    red = getColorByName('red')
    yellow = getColorByName('yellow')

    # return a list of opened molecules
    for mol in openModels.list(modelTypes=[Molecule]):
        mol.color = red # change model color to be red
        atoms = mol.atoms
        for atom in atoms:
            if atom.name == 'CA':
                atom.color = yellow
