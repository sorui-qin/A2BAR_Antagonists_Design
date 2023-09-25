with open(r'D:\Research\A2B\generate_overfit.sh','w+') as re:
    for i in range(1,101):
        re.write('python sample_scaffolds.py -m trained_models/a2banta.90.model -i sca_benzyl/scaffold_{:03d}.smi -o sca_benzyl/validation/overfit/generation_{}.csv -r 16 -n 16 -d multi --of csv'.format(i-1,i)+'\n')