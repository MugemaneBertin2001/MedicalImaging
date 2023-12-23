def calculate_delta_k(fov):
    """Calculates spacing between samples in k-space (Δk) based on FOV."""
    delta_k = 1 / fov
    return delta_k

def calculate_k_fov(delta_k):
    """Calculates k-space field-of-view (kFOV) based on Δk."""
    k_fov = 1 / delta_k
    return k_fov

def calculate_pixel_width(k_fov):
    """Calculates pixel width (Δw) based on k-space field-of-view (kFOV)."""
    delta_w = 1 / k_fov
    return delta_w

if __name__ == "__main__":
    # Input the field-of-view (FOV) in centimeters
    fov = float(input("Enter FOV in cm: "))

    # Calculate Δk and kFOV
    delta_k = calculate_delta_k(fov)
    k_fov = calculate_k_fov(delta_k)

    # Calculate Δw based on kFOV
    delta_w = calculate_pixel_width(k_fov)

    print(f"The spacing between samples in k-space (Δk) is approximately {delta_k:.4f}")
    print(f"The k-space field-of-view (kFOV) is approximately {k_fov:.4f}")
    print(f"The pixel width (Δw) is approximately {delta_w:.4f}")
