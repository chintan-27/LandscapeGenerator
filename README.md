# ColorScaper (Originally called LandscapeGenerator)

#Inspiration
Our inspiration came from wanting to explore the unknown. In particular, we thought that human imagination was the most unknown space. So we created an AI website that can visually express the landscape that people imagine. 

#What it does
ColorScope helps us to explore unknown landscapes using AI through color code data that is received in the form of five colors from the users. It can also function to know various colors of nature. It helps you build landscapes that may not be present on our planet. It lets you peek into your realm of imagination on how other planets or places look like.

#How we built it
We are using conditional generative adversarial networks (cGANs) to accomplish this task. GANs are one of the most effective machine-learning models for new controlled data generation. We used a Dataset with about 4000+ landscape images and the top 5 most abundant colors in those images as input to the GAN. We rescaled and preprocessed the images using OpenCV to a uniform size. We used TensorFlow to train the model. We are using deep branched convolutional network
