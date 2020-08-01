# Splice
Declarative web framework for fast application development. I'm just starting out with this one, so expect lots of features soon!

![preview](https://i.imgur.com/2MMOGQh.png)

## How to use

The syntax is inspired by SwiftUI and for now is fully presented in the page_example.py.

### Install dependencies

```pip install flask```

### Run the example

```python app.py```

### Configure main page

If you want another file to be the entry point to your prototype, then specify it in ```settings.py```:

```main_page = 'your_app_name'```

Don't forget, that your splice declarations shoud be wrapped in the ```App``` view and assigned to ```body``` variable. Otherwise flask will not recognize your code.

```body = App(your_main_view)```

### Have fun

That's it! If you have any questions or ideas, feel free to contact me: subatiq@gmail.com

