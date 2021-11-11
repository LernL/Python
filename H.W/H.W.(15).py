dict={
    'user_0':{
        'name':'Alexey',
        'surname':'Kosenko',
        'housenumber':14.5,
        'yourage':14
        },
    'user_1':{
        'name':'Illia',
        'surname':'Katerinych',
        'housenumber':13.7,
        'yourage':15
        }
    }
for i,b in dict.items():
    print(f"{i}:")
    for a,c in b.items():
        print(f"\t{a}: {c}")
