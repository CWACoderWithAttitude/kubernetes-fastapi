from fastapi import APIRouter

from service.core.models.output import MessageOutput
from service.core.models.input import MessageInput
from service.core.logic.business_logic import run_prime_factor_calculation
import os

router = APIRouter()
DEFAULT_MESSAGE = 'DEFAULT_MESSAGE'

def read_env():
    print('read_env...')
    default_message='nix'  
    print_env()
    if DEFAULT_MESSAGE in os.environ:
        default_message = os.environ[DEFAULT_MESSAGE]
    print (f'default message: {default_message}')
    
    return default_message

def read_from_env(key):
    print('read_from_env...')
    value='n/a'  
    print_env()
    if key in os.environ:
        value = os.environ[key]
        print (f'value: {value}')
    print(f'read_from_env: {key} ==> {value}')
    return value

def print_env():
    for k in os.environ:
        print('print_env > ', k, ' ==> ', os.environ[k])

@router.get("/hej", tags=["example get"])
def example_get():
     """
     Say hej!

     This will greet you properly

     And this path operation will:
     * return "hej!"
     """
     msg = read_env()
     return {"msg": f"Hey {msg}"}

@router.post("/hello", response_model=MessageOutput, tags=["hello post"])
def hello_endpoint(inputs: MessageInput):
    """
    Respond to requests on the hello endpoint

    """

    #"message2": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
    n, largest_prime_factor, elapsed_time = run_prime_factor_calculation()
    msg1 = read_from_env('MSG1')
    msg2 = read_from_env('MSG2')
    msg2 = msg2%(n, largest_prime_factor, elapsed_time)
    return {
        "message1": msg1,
        "message2": msg2,
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }
