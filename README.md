# Parallel Image Processing Pipeline

## Introduction  
Image processing is a crucial task in computer vision, AI, and data analysis. However, applying filters to a large dataset of images can be computationally expensive.  

This project aims to accelerate image filtering using Python’s `multiprocessing` module. By leveraging parallel processing, we can improve efficiency and reduce execution time.  

This document explains the code structure, parallelization approach, and benchmarking results comparing the serial and parallel versions.

---

## Problem Description  
This project consists of:  
1. **Downloading images from a `.tsv` dataset** containing image URLs.  
2. **Applying image processing filters**, specifically:  
   - **Grayscale** (converts the image to black and white).  
   - **Blur** (reduces details using a Gaussian filter).  
   - **Edge detection** (highlights contours using the Canny operator).  
3. **Implementing both serial and parallel versions** to process images.  
4. **Comparing performance** when running filters with 1, 2, 3, 4, and 6 processes.  

---

## Code Explanation  

The code is divided into two main functions:

### **1. Load the image dataset (`load_photo_dataset`)**  
This function searches for a `photos.tsv` file, extracts the necessary columns (`photo_id` and `photo_image_url`), and returns a Pandas DataFrame.

```python
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
