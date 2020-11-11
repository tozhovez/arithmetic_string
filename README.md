
# Arithmetic String

**The following is your assignment:**

**The API server you will build will act as a calculator.**

1. **Using any framework you choose, build an API server with a single endpoint named “calculate”. This means that the requests should be routed to http://&lt;server&gt;/calculate.**
2. **This endpoint should be able to receive a POST request with a JSON body in the following form:**

**{“data”: &lt;String&gt;}**

**The string in the data field will be a base64 encoded arithmetic string \(something like 2+2 or 2-2+1\) like the following: Misy \(Which is 2+2 b**ase64 encoded**\).**

1. **The API should now calculate the arithmetic string and return the result in a JSON response as following:**

**{“result”: 4}**

# Setup
## Use Python 3.7+ (Python 3.8.5)
## Clone the repo, create virtualenv if necessary.

[https://github.com/tozhovez/arithmetic\_string.git](https://github.com/tozhovez/arithmetic_string.git)

## Install the dependencies, listed in the requirements.txt file:
```bash
$ cd arithmetic_string
$ python -m pip install -r requirements.txt
```

## Run app server:


```bash
$ cd arithmetic_string/calculator-service
$ python based_api_server/main.py

======== Running on http://127.0.0.1:50772 ========
(Press CTRL+C to quit)

```

## Run app client:

```bash
$ cd arithmetic_string/calculator-service
$ python calculate_client_web/main.py

======== Running on http://127.0.0.1:8080 ========
(Press CTRL+C to quit)

```

##Open browser client :

```text
http://127.0.0.1:8080
```

## Run shell client:
```bash
$ cd arithmetic_string/calculator-service
$ python based_api_client/client.py

(1+1-1/2)-(0.1*10-1)-(-1+1*2-1)*2
{"result": 1.5}

```

## 

### Requirements

* [aiohttp](https://github.com/KeepSafe/aiohttp)
* [aiohttp\_jinja2](https://github.com/aio-libs/aiohttp_jinja2)

