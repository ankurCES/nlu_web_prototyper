# NLU Web Prototype Creator

### Introduction

Airbnb created a prototyping tool that takes wireframes drawn on a whiteboard and converts them into html. In this project I have taken a slightly different approach of taking natural language into creating simple prototypes. 
Simple commands like `add an image` or `add a text box` can create quick and dirty prototypes. 

It's still in very early stages of development and is missing a lot of features. Whiteboard image to html is also something that is still being worked on and I will have that here soon.

If you do find this useful please help in making this better.
Happy Coding!!


### See it in action

[<img src="https://img.youtube.com/vi/XUyV54iWvgA/maxresdefault.jpg" width="50%">](https://youtu.be/XUyV54iWvgA)

### Dependencies

- Node JS
- Python 3+


### Steps To Run

#### Install Python Dependencies
```
$> pip install SimpleWebSocketServer
$> pip install websocket_client
$> pip install snips-nlu
$> snips-nlu download en
```

#### Install Node Dependencies
```
$> npm install -g gatsby-cli
```

#### Running the NLU Intent provider

`$> python get_intent.py`

#### Running the Web Builder

`$> python ws_client.py`

#### Running the Gatsby project

```
$> cd web-builder
$web-builder> gatsby develop
```

Open the browser and visit [http://localhost:8000](http://localhost:8000)


### To see the builder in action

Go to the prompt where the Intent provider is running

As an example try the following in sequence
```
add a card
add a title
add an image
```

You should see the web preview being live reloaded in the browser
