import marimo

__generated_with = "0.11.25"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    mo.md("# Time Delta")
    return (mo,)


@app.cell
def _():
    import datetime
    import time

    start_time = datetime.datetime.now()
    time.sleep(.5)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    duration
    return datetime, duration, end_time, start_time, time


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
