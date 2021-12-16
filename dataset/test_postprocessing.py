import pickle
import os

folder = './work_dirs/nucleus/'

result = open(folder + 'result.pkl', 'rb')
annos = pickle.load(result)

with open(folder + 'answer.json', "w") as f:
    f.write("[\n")
    first = True
    for i in range(6):
        size = len(annos[i][0][0]) 
        for j in range(size):
            [x1, y1, x2, y2, s] = annos[i][0][0][j]
            if i == 0 and j == 0:
                f.write("   {\n")
            else:
                f.write(", \n   {\n")
            f.write("       \"image_id\": " + str(i + 1))
            f.write(", \n")

            f.write("       \"score\": " + str(s))
            f.write(", \n")

            f.write("       \"category_id\": 1")
            f.write(", \n")

            f.write("       \"bbox\": [\n")
            f.write("           " + str(x1) + ", \n")
            f.write("           " + str(y1) + ", \n")
            f.write("           " + str(x2 - x1) + ", \n")
            f.write("           " + str(y2 - y1) + "\n")
            f.write("       ], \n")

            f.write("       \"segmentation\": \n")
            st = str(annos[i][1][0][j])
            st = st.replace("b\'", "\"")
            st = st.replace("\'", "\"")

            f.write("           " + st)

            f.write("\n")
            f.write("   }")
    f.write("\n]\n")