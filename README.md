# PARTY3

Make sure you know what your third-party services are up to.

## Usage

Party3 comes with some services to get you started, here's a list:

 - none so far! But I'm adding them.

### Configuration

Configuration is taken care of completely through environment variables:

 - `PARTY3_SERVICES`: A comma-separated list of services (python files in
   `party3/services`)

Services/notifiers may have their own environment variables, and will notify
you (or raise errors) if their requirements aren't satistified.

### Writing Services

Services are just python files sitting in `party3/services/`. Here's a silly
one that will warn you randomly (it would live in `party3/services/random.py`):

    import random
    from party3.supplies import notify

    def run():
        if random.choice([True, False]):
            notify('Random provider is down.')

Then you would change your `PARTY3_SERVICES` variable to include it:

     PARTY3_SERVICES=...,random

Then just restart your worker/scheduler processes, and it will Just Work(TM).

## Deploying

This project is designed, in a fit of utter irony, to be deployed to Heroku.
There's no web role, so to keep it in the free tier, just spin up a scheduler
(but only one) and add workers if you need to.
