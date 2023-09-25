import pandas as pd
import rdkit
import rdkit.Chem as rkc

filename = r'D:\Research\A2B\Molecules\benzyl_sca\overall_gene.csv'

def standrad_smi(smile):
    return rkc.MolToSmiles(rkc.MolFromSmiles(smile))

def valid_smi(smi):
    if not "*" in smi:
        return smi

def delete_same(li):
    fin_li=[]
    for smi in li:
        fin_li.append(valid_smi(standrad_smi(smi)))
        del_li = sorted(set(fin_li),key=fin_li.index)
        del_li = filter(None, del_li)
    return del_li

def combine(filename):
    df = pd.read_csv(filename)
    standrad_li = delete_same(df["smiles"].values.tolist())
    with open(filename.replace('csv','smi'),'w+', encoding="utf-8", ) as fi:
        for smi in standrad_li:
            fi.write(smi+'\n')
        fi.close()

combine(filename)

