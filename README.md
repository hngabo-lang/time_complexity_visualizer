# activity

Flask app that times algorithms across increasing input sizes, plots the
results, and can save runs to a SQLite database behind JWT login.

## How to run it

```
pip install -r requirements.txt
python app.py
```

Server runs at `http://127.0.0.1:5000`.

## Endpoints

- `GET /`
  Lists available algorithms and usage.

- `GET /analyze?algo=<name>&step=<int>&n_max=<int>`
  Runs the algorithm across increasing input sizes and returns a base64
  plot image. No login required.

- `POST /login`
  HTTP Basic Auth (`-u username:password`).
  Returns `{"access_token": "..."}` on success, `401` otherwise.
  Token expires 15 minutes after login by default.

- `POST /analyze/save?algo=<name>&step=<int>&n_max=<int>`
  Requires header `Authorization: Bearer <token>`.
  Runs the algorithm, then saves the run to `analysis.db` (table `analysis`).

## Available algorithms

`binary_search`, `linear_search`, `bubble_sort`, `nested_loop`,
`selection_sort`, `insertion_sort`, `merge_sort`, plus whatever is defined
in `stack_queue.py` (`STACK_QUEUE_ALGORITHMS`).

## Quick test (PowerShell)

```powershell
# 1. login
curl.exe -X POST http://127.0.0.1:5000/login -u Henry:Henry123

# copy the access_token value from the response, then:

# 2. analyze and save in one step
curl.exe -X POST "http://127.0.0.1:5000/analyze/save?algo=bubble_sort&step=100&n_max=1000" -H "Authorization: Bearer YOUR_TOKEN"
```
