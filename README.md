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
```

## Explanation
**Folder Creation:** The function ensures the image folder exists before downloading.

**Iterating Over the Dataset:** The function loops through the photo_df DataFrame to extract photo_id and photo_image_url.

**Downloading Images:**

Each image is downloaded using requests.get().

The image is saved locally using the photo_id as the filename.

**Error Handling:**

If an image URL is missing, the function skips that image.

A try-except block is used to handle request errors and avoid interruptions.

**Download Limit:**

The function stops downloading images once the max_images limit (150) is reached.

## Image Download and Processing Script
**Code Execution**
The main section of the script runs the functions:

```python
if __name__ == "__main__":
    image_folder = "../images"  # Directory for storing images
    
    photos_df = load_photo_dataset(image_folder)
    
    if photos_df is not None:
        image_paths = download_images(photos_df, image_folder)
        print(f"Found {len(image_paths)} images for processing.")
```
# Explanation:
**Defines the image storage directory:** image_folder is set to "../images".

**Loads the image dataset:** The load_photo_dataset() function loads the dataset containing information about the images.

**If images are available, it proceeds to download them:** The download_images() function handles the download.

## Project Approach
**Serial Implementation:**
Images are downloaded and processed sequentially.

Filters are applied one by one to all images.

**Limitation:** It takes longer since it only uses a single CPU core.

## Parallel Implementation:
Uses multiprocessing.Pool to distribute tasks across multiple processes.

Images are processed in parallel, reducing execution time.

**Advantage:** Better CPU resource utilization.

## Benchmarking Results

Execution time was measured with 1, 2, 3, 4, and 6 processes.

| Number of Processes | Execution Time (seconds) |
|---------------------|--------------------------|
| 1 process           | 64.00 s                   |
| 2 processes         | 39.79 s                   |
| 3 processes         | 33.02 s                   |
| 4 processes         | 29.76 s                   |
| 6 processes         | 28.70 s                   |

*(Execution time depends on hardware and dataset size)*

## Conclusions

- **Multiprocessing improves performance**: The parallel implementation significantly reduced processing time compared to the serial version.

- **Optimal number of processes varies**: Beyond a certain number of processes (usually equal to the number of CPU cores), performance stops improving due to task management overhead.

### Factors affecting performance:
- The number of images and their size.
- CPU workload.
- The number of parallel processes used.

### Potential improvements:
- Optimization could be done using `concurrent.futures.ProcessPoolExecutor` or batch-processing strategies.


