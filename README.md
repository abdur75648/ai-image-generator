# ai-image-generator
Generate artistic images using Neural Style Transfer Algorithm

Try deployed webapp - [Heroku (Depcrecated)](https://ai-image-generator.herokuapp.com) | [Render (Latest)](https://ai-image-style-generator.onrender.com/)

## Usage
* It is a Flask-based Web Application
* To make this practical, I've uploaded pre-trained models of some common styles (Because training the model everytime one wants to use this app requires much more resouces)
* You need to upload a content image and a style image of your choice.
* Submit & wait for few seconds. The output image will appear o the screen 🎉
* Enjoy generating several cool images 🎊

## References
* This project is the implementation of the paper [_Image Style Transfer Using Convolutional Neural Networks_](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)
* Pre-trained models can be found [here](https://github.com/jcjohnson/fast-neural-style) & can be placed in static/models folder
* A step-by-step guide is given in [_this article_](https://towardsdatascience.com/building-deploying-a-neural-style-transfer-app-with-pre-trained-models-661bbefc74cd)
