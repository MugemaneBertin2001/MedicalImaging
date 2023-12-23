def calculate_roi_size_in_k_space(roi_width, roi_height, fov):
    """Calculates the size of ROI in k-space based on ROI dimensions and FOV."""
    num_pixels_x = roi_width / fov
    num_pixels_y = roi_height / fov

    k_fov_x = num_pixels_x / fov
    k_fov_y = num_pixels_y / fov

    return k_fov_x, k_fov_y

if __name__ == "__main__":
    # Input the dimensions of the ROI in the image (in mm)
    roi_width = float(input("Enter ROI width in mm: "))
    roi_height = float(input("Enter ROI height in mm: "))

    # Input the field-of-view (FOV) in mm
    fov = float(input("Enter FOV in mm: "))

    # Calculate the ROI size in k-space
    k_fov_x, k_fov_y = calculate_roi_size_in_k_space(roi_width, roi_height, fov)

    print(f"The ROI size in k-space (kFOV) in x-direction is approximately {k_fov_x:.4f}")
    print(f"The ROI size in k-space (kFOV) in y-direction is approximately {k_fov_y:.4f}")
