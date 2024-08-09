import os
import pickle
# Define the base directory where your images are stored
base_dir = 'D:\\U\\7. Septimo\\RI\\ir24a\\week14\\caltech-101'

# List to hold image paths
train_labels = []

# Traverse the directory structure
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.jpg'):  # Assuming all images are in jpg format
            relative_path = os.path.relpath(os.path.join(root, file), base_dir)
            train_labels.append(relative_path)

# Save the labels to a pickle file
with open('train_labels_cate.pkl', 'wb') as f:
    pickle.dump(train_labels, f)