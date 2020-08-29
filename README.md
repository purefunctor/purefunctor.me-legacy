# purefunctor.me
My personal portfolio website that I've written to practice Django, which you can visit through [purefunctor.me](http://purefunctor.me).

# Development Setup
This project uses `pipenv` to set up a development environment; using Linux is also recommended.

Clone the repository and set up the environment.
```bash
$ git clone https://github.com/PureFunctor/purefunctor.me
$ cd purefunctor.me
$ pipenv sync --dev
$ pipenv run precommit
```

Set up the environment variables by creating a `.env` file.
```
DEBUG=True
SECRET_KEY={RANDOM_CHARACTERS}
```

Run the development server then visit the given URL.
```bash
$ pipenv run start
```
