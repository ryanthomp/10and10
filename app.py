from flask import Flask, render_template
import period
import asyncio

app = Flask(__name__)
check = period.Time().check()


async def time():
    print("time")
    print(check)
    if check is True:
        print('GREEN')
        return "LightGreen"
    elif check is False:
        print("RED")
        return "LightCoral"


loop = asyncio.get_event_loop()


@app.route('/')
def index():
    color = loop.run_until_complete(time())
    print(color)
    return render_template('index.html', color=color)


if __name__ == '__main__':
    app.run()
