def tuner(**kwargs):
    """keyword argument function"""
    brightnesss = kwargs.get('brightness', 0)
    hue = kwargs.get('hue', 0)
    contrast = kwargs.get('contrast', 0)
    print(brightnesss, hue, contrast)



tuner()
tuner(brightness=.78, hue=.76)
tuner(brightness=.89, hue=.78, contrast=90)  # keywords argument
