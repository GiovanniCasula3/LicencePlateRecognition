import os 
import joblib
import segment_marging
import connected_regions

# Load the model
current_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(current_dir, "models", "svc", "model.pkl")
svc_model = joblib.load(model_path)

classification_results = []
for each_character in segment_marging.characters:
    each_character = each_character.reshape(1, -1)
    result = svc_model.predict(each_character)
    classification_results.append(result)

print(classification_results)
plate_string = ""
for eachPredict in classification_results:
    plate_string += eachPredict[0]
    
print(plate_string)

column_list_copy = segment_marging.column_list[:]
segment_marging.column_list.sort()
rightplate_string = ""
for each in segment_marging.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]

print(rightplate_string)
