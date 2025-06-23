def print_results(results, results_stats, model_arch, print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary of the results.

    Args:
    - results (dict): Dictionary containing results of classification.
    - results_stats (dict): Dictionary containing statistics of the classification results.
    - model_arch (str): Architecture of CNN model used (vgg, alexnet, resnet).
    - print_incorrect_dogs (bool): Whether to print misclassified dogs (default: False).
    - print_incorrect_breed (bool): Whether to print misclassified breeds (default: False).
    """
    print(f"\nCNN Model Architecture: {model_arch.upper()}\n")
    
    # Overall counts
    n_images = len(results)
    n_dog_images = results_stats['n_dogs_img']
    n_notdog_images = results_stats['n_notdogs_img']
    
    print(f"Number of Images: {n_images}")
    print(f"Number of Dog Images: {n_dog_images}")
    print(f"Number of \"Not-a\" Dog Images: {n_notdog_images}\n")
    
    # Results statistics
    for key, value in results_stats.items():
        if key.startswith('p'):  # Printing percentage statistics
            print(f"{key}: {value:.1f}%")
    
    # Printing misclassifications
    if print_incorrect_dogs:
        print("\nMisclassified Dogs:")
        for key in results:
            if sum(results[key][3:]) == 1:  # Misclassified as dog
                print(f"Pet Image: {key}, Classifier Labels: {results[key][1]}")
    
    if print_incorrect_breed:
        print("\nMisclassified Breed's of Dog:")
        for key in results:
            if sum(results[key][3:]) == 2 and results[key][2] == 0:  # Misclassified breed
                print(f"Pet Image: {key}, Classifier Labels: {results[key][1]}")
