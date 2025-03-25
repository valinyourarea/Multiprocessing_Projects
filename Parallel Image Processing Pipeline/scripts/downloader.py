import os
import pandas as pd
import glob
import requests
from bs4 import BeautifulSoup

def load_photo_dataset(path='../images'):
    """Load the photo dataset and extract relevant information."""
    photo_file = glob.glob(os.path.join(path, "photos.tsv*"))
    
    if not photo_file:
        print("Error: No photos.tsv file found!")
        return None
    
    df = pd.read_csv(photo_file[0], sep='\t', header=0)
    
    # Extract only necessary columns
    if 'photo_id' in df.columns and 'photo_image_url' in df.columns:
        df = df[['photo_id', 'photo_image_url']]
    else:
        print("Error: Required columns not found in photos dataset!")
        return None
    
    return df



def download_images(photo_df, image_folder="../images", max_images=150):
    """Download up to `max_images` images after extracting direct links."""
    os.makedirs(image_folder, exist_ok=True)
    image_paths = []
    count = 0  # Counter to limit downloads
    
    for _, row in photo_df.iterrows():
        if count >= max_images:
            break  # Stop downloading after reaching the limit

        photo_id = row['photo_id']
        
        image_url = row['photo_image_url']
        if not image_url:
            print(f"Skipping {photo_id}: Could not extract image URL")
            continue
        
        local_path = os.path.join(image_folder, f"{photo_id}.jpg")
        
        try:
            response = requests.get(image_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(local_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded {count + 1}: {local_path}")
                image_paths.append(local_path)
                count += 1  # Increment counter
            else:
                print(f"Failed to download {image_url}")
        except requests.RequestException as e:
            print(f"Error downloading {image_url}: {e}")
    
    print(f"Download complete. {count} images saved.")
    return image_paths

if __name__ == "__main__":
    image_folder = "../images"  # Directory containing images
    
    photos_df = load_photo_dataset(image_folder)
    
    if photos_df is not None:
        image_paths = download_images(photos_df, image_folder)
        print(f"Found {len(image_paths)} images for processing.")
    