import os
import shutil

# dataset_path ='WOTR\JPEGImages'


# Function to divide dataset into groups of 4500 images
def divide_dataset(dataset_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get list of all image files in dataset directory
    image_files = [f for f in os.listdir(dataset_path) if os.path.isfile(os.path.join(dataset_path, f))]
    num_images = len(image_files)
    images_per_folder = 4700
    num_folders = (num_images + images_per_folder - 1) // images_per_folder
    
    # Loop through each group of 4500 images and save them in separate folders
    for i in range(num_folders):
        start_idx = i * images_per_folder
        end_idx = min((i + 1) * images_per_folder, num_images)
        folder_name = f"folder_Annotations{i+1}"
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path)
        
        # Copy images to the current folder
        for j in range(start_idx, end_idx):
            image_name = image_files[j]
            src_image_path = os.path.join(dataset_path, image_name)
            dest_image_path = os.path.join(folder_path, image_name)
            shutil.copy(src_image_path, dest_image_path)
        
        print(f"Saved {end_idx - start_idx} images to {folder_name}")

# Example usage
dataset_path = "WOTR/Annotations"
output_dir = "Output_Annotations"
divide_dataset(dataset_path, output_dir)
