def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image
    
    Args:
        filename: The filename of a BMP file

    Returns:
        A tuple containing two integers with the width and height in pixels

    raises:
        ValueError: If the file was not a BMP file
        OSError: If there was a problem reading the file.

    """

    with open(filename, mode='rb', encoding='rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError(f'{filename} is not a BMP file.')

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)
        return (_b)

