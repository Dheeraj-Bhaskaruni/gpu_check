import tensorflow as tf

# Check GPUs available
gpus = tf.config.list_physical_devices('GPU')

if len(gpus) > 0:
    print(f"Number of GPU(s) available: {len(gpus)}")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPU available.")
