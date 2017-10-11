# Features
Hair_color = {
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG",
    "Blonde": "TTAGCTATCGC"}

Face_shape={
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA",
}

Eye_color={
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC",
}

Gender={
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC",
}


Race={
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG",
}


# Suspects
Eva={
    "Gender": "Female",
    "Race": "White",
    "Hair_color": "Blonde",
    "Eye_color": "Blue",
    "Face_shape": "Oval",
}


Larisa={
    "Gender": "Female",
    "Race": "White",
    "Hair_color": "Brown",
    "Eye_color": "Brown",
    "Face_shape": "Oval",
}


Matej={
    "Gender": "Male",
    "Race": "White",
    "Hair_color": "Black",
    "Eye_color": "Blue",
    "Face_shape": "Oval",
}


Miha={
    "Gender": "Male",
    "Race": "White",
    "Hair_color": "Brown",
    "Eye_color": "Green",
    "Face_shape": "Square",
}

# found dna

with open("dna.txt","r") as f:
    dna=f.read()


features_names = ["Hair_color", "Face_shape","Eye_color","Gender","Race"]
features_list = [Hair_color,Face_shape,Eye_color,Gender,Race]
feature_with_name = zip(features_names, features_list)


suspects_names = ["Miha", "Eva", "Larisa","Matej"]
suspects_list = [Miha, Eva, Larisa, Matej]
suspects_with_name = zip(suspects_names, suspects_list)


found_features = {}

# finding features:
for name, feature in feature_with_name:
    for key, val in feature.iteritems():
        if val in dna:
            found_features[name]=key
            print "Found ", name, ": ", key
            break


for name, suspect in suspects_with_name:
    print
    print "Examining", name
    for feature,suspect_value in suspect.iteritems():
        print "Checking", feature
        if found_features[feature] != suspect_value:
            print "No Match"
            print "-"*10
            break
    else:
        print "The criminal was:", name
        break
