from django.shortcuts import render
from .forms import PuzzleForm
import math
import random

def index(request):
    result = None
    
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']
            
            # Number Puzzle
            number_result = process_number_puzzle(number)
            
            # Text Puzzle
            text_result = process_text_puzzle(text)
            
            # Treasure Hunt
            treasure_result = treasure_hunt_simulation()
            
            result = {
                'number_result': number_result,
                'text_result': text_result,
                'treasure_result': treasure_result,
            }
    else:
        form = PuzzleForm()
    
    return render(request, 'puzzle/index.html', {
        'form': form,
        'result': result
    })


def process_number_puzzle(number):
    """
    Determine if number is even or odd.
    If even: calculate square root
    If odd: calculate cube
    """
    if number % 2 == 0:
        # Even number - calculate square root
        sqrt_result = math.sqrt(number)
        return {
            'type': 'even',
            'number': number,
            'operation': 'Square Root',
            'result': sqrt_result
        }
    else:
        # Odd number - calculate cube
        cube_result = number ** 3
        return {
            'type': 'odd',
            'number': number,
            'operation': 'Cube',
            'result': cube_result
        }


def process_text_puzzle(text):
    """
    Convert text to binary and count vowels
    """
    # Convert to binary
    binary = ' '.join(format(ord(char), '08b') for char in text)
    
    # Count vowels
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)
    
    return {
        'original_text': text,
        'binary': binary,
        'vowel_count': vowel_count
    }


def treasure_hunt_simulation():
    """
    Simulate guessing a random number (1-100) in 5 tries or less
    """
    target = random.randint(1, 100)
    max_tries = 5
    low = 1
    high = 100
    attempts = []
    
    for attempt in range(1, max_tries + 1):
        # Binary search strategy for better chances
        guess = (low + high) // 2
        attempts.append({
            'attempt_number': attempt,
            'guess': guess,
            'target': target
        })
        
        if guess == target:
            return {
                'success': True,
                'target': target,
                'attempts': attempts,
                'total_tries': attempt,
                'message': f'🎉 Treasure found! The number was {target}!'
            }
        elif guess < target:
            low = guess + 1
            attempts[-1]['hint'] = 'Too low!'
        else:
            high = guess - 1
            attempts[-1]['hint'] = 'Too high!'
    
    return {
        'success': False,
        'target': target,
        'attempts': attempts,
        'total_tries': max_tries,
        'message': f'❌ Treasure not found. The number was {target}.'
    }