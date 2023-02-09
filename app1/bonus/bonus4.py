contents = ['Rhaydrick Sandokhan Pinehiro Teixeira Tavares', 'Filipa Susana Gonçalves Ribeiro', 'Moreira de Cônegos & Lordelo - GMR']

filenames = ['doc.txt','report.txt','presentation.txt']

for content,filename in zip(contents,filenames):
    with open(f"./files/{filename}", 'w') as file:
        file.writelines(content)