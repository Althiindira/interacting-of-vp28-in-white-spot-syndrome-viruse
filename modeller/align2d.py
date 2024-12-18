from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='2ed6', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2ed6A', atom_files='2ed6.pdb')
aln.append(file='querysequence.ali', align_codes='querysequence')
aln.align2d(max_gap_length=50)
aln.write(file='querysequence-2ed6A.ali', alignment_format='PIR')
aln.write(file='querysequence-2ed6A.pap', alignment_format='PAP')
