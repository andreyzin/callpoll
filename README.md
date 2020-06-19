# CallPoll

Basic functionality of redirecting CallBack to LongPoll.

Is used mainly for easy testing or if there is no python hosting.

Server side is written in php

## Some Docs Here
- Firsly you need to init your CallPoll with:
    ```python
    app = CallPoll("SERVER_NAME")
    ```
    SERVER_NAME should be uniq and it is better to use "favorite_name"+"random_sequence".

- Then just add decorator `@callpoll.route` to any function, which should recieve one argument `event`
    ```
    @app.route
    def processing(event):
        return "Hello"
    ```

- And finally launch it with
    ```python
    app.run()
    ```