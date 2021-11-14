# HACKUTD-RKD

Rishabh Vemparala (rishixyz9)
Dax Collison (codeCollision4)
Kanishk Garg (KanishkGar)

## Inspiration
Millions of people each year are afflicted with Melanoma and we wanted to try to build a tool that would help easily quell worries people may have about their skin.
## What it does
Our app uses machine learning to predict on an image and classify it as melanoma or not. It can either take in a saved image file or it can take an image from a webcam.
## How we built it
We used Tensorflow and the HAM10k melanoma dataset to train the model. We used Django to make the website and OpenCV to take in webcam video +  process the image.
## Challenges we ran into
Our model was not predicting properly after we had trained, saved, and reloaded it. It took us many hours, but eventually we managed to get it to work by training the model in firefox instead of chrome. Also, a comment was once causing a bug in our code which was frustrating to fix.
## Accomplishments that we're proud of
We're proud of eventually training the model to have >90% validation accuracy and deploying the model to the website. Also, we're proud of being able to display a live video feed to the website and predict based on snapshots of the feed.
## What we learned
We learned how to use OpenCV to get webcam footage and how to transfer data with urls between the different pages in our app.
## What's next for Melanoma Detection
Next, we would like to implement live detection and transition it so that it can work using a mobile camera as well.


