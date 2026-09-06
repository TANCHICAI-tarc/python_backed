from fastapi import FastAPI
from scraper_logic import run_my_python_task

app = FastAPI()


@app.get("/run-python")
def trigger_python():
  result = run_my_python_task()
  return result