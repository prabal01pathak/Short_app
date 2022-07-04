
![Logo](https://avatars.githubusercontent.com/u/10178994?s=200)
# SHORT VIDEO

Upload, View and Delete short videos.


## Authors

- [@prabalPathak](https://www.github.com/prabal01pathak)


## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Usage/Examples

```sh
python3 manage.py runserver
```
or
```bash
python3 manage.py runserver --host ${HOST} --port ${PORT}
```


## Lessons Learned
Practice Makes Perfect
## 🛠 Skills
- Python3
- FastAPI
- Strawberry


## Tech Stack
**Programming Language** - Python3

**Framework** - FastAPI

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Documentation

[Documentation](https://linktodocumentation)


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Installation

```bash
  pip3 install poetry
  poetry shell
  poetry install
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/prabal01pathak/short_video.git
```

Go to the project directory

```bash
  cd short_video
```

## Install dependencies

### Install poetry (Optional)
```bash
pip3 install poetry
```

```bash
  poetry install
```

Start the server

```bash
  python3 manage.py runserver
```


