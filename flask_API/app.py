from flask import Flask,json, render_template, request, send_file, jsonify
import cv2
import os
import tensorflow as tf
from tensorflow.keras import layers
from IPython import display
import numpy as np
import pandas as pd
import os
import random
import extcolors
from PIL import Image
import math


def replaceColor(orig_color, replacement_color, data):
    r1, g1, b1 = orig_color[0], orig_color[1], orig_color[2] 
    r2, g2, b2 = replacement_color[0], replacement_color[1], replacement_color[2] 

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]
    return data
    
    
def detectSimColors(colors):
    colorsSim = []
    colorsTemp = []
    for color1 in colors:
        sim = []
        for color2 in colors:
            if(color2[0] not in colorsTemp):
                if(math.dist(list(color1[0]), list(color2[0])) < 150):
                    if(color2[0] not in colorsTemp):
                        sim.append(color2[0])
                        colorsTemp.append(color2[0])
        if(len(sim) > 0):
            colorsSim.append(sim)
    return colorsSim

def predict(colors, latent_dim = 200, outputPath = "images/Output.png"):
    num_examples_to_generate = 1
    latent_dim = 200
    noise = tf.random.normal([num_examples_to_generate, latent_dim])
    labels = np.array([colors]) / 255
    model = tf.keras.models.load_model("LandScapeGanFinal.h5")
    predictions = model([noise, labels], training=False)
    pred = ((predictions[0].numpy() + 1) * 127.5).astype(np.uint8)
    # pred = cv2.detailEnhance(pred, sigma_s=6, sigma_r=1.0)
    rgb = cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(pred)
    colors, _ = extcolors.extract_from_image(im_pil)
    count = 0
    labels = (labels * 255).astype(np.uint8)
#     colorsSim = detectSimColors(colors)

#     for color in colorsSim:
#         print(color)
#         for i in color:
#             rgb = replaceColor(i, labels[0][count * 3: (count * 3) + 3], rgb)
#         count += 1
#         if(count > 4):
#             break

    original = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite("static/images/output.png", original)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    gray = cv2.merge([gray,gray,gray])

    # create 1D LUT
    # create 1 pixel blue image
    one = np.full((1, 1, 3), tuple(labels[0][0:3]), np.uint8)
    two = np.full((1, 1, 3), tuple(labels[0][3:6]), np.uint8)
    three  = np.full((1, 1, 3), tuple(labels[0][6:9]), np.uint8)

    # append the 3 images
    lut = np.concatenate((one, two, three), axis=0)

    # resize lut to 256 values
    lut = cv2.resize(lut, (1,256), interpolation=cv2.INTER_CUBIC)

    # apply lut to gray
    result = cv2.LUT(gray, lut)
    result2 = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
    alpha = 0.5
    img3 = np.uint8(result*alpha + original*(1-alpha))
    cv2.imwrite("static/images/output1.png", result2)
    cv2.imwrite("static/images/output2.png", img3)
    return outputPath

#create instance of Flask app
# PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


  
@app.route("/predict", methods=['POST'])
def all():
    x = request.data.decode('utf8').replace("'", '"')
    colors = eval(x)["colors"]
    # data = json.loads(x)
    # colors = eval(request.form['colors'])
    colorList = []
    for i in colors:
        colorList += list(i)
    colorList.append(random.randint(0, 255))
    filename = predict(colorList)
    # response = jsonify(link = "http:1/images/Output2.png")
    # response.headers.add("Access-Control-Allow-Origin", "*")

    # return {'c': eval(request.form['colors'])}
    # # print(type(eval(x)))
    return {}
    


if __name__ == "__main__":
    app.run(debug=True)