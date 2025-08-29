from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

class DiceSimulator:
    def __init__(self):
        self.history = []
    
    def roll_dice(self, num_dice=1, num_sides=6):
        """Roll specified number of dice with specified number of sides"""
        if num_dice < 1 or num_dice > 10:
            raise ValueError("Number of dice must be between 1 and 10")
        if num_sides < 2 or num_sides > 100:
            raise ValueError("Number of sides must be between 2 and 100")
        
        results = []
        for _ in range(num_dice):
            roll = random.randint(1, num_sides)
            results.append(roll)
        
        # Add to history
        roll_data = {
            'dice': num_dice,
            'sides': num_sides,
            'results': results,
            'total': sum(results)
        }
        self.history.append(roll_data)
        
        # Keep only last 20 rolls
        if len(self.history) > 20:
            self.history.pop(0)
        
        return roll_data
    
    def get_statistics(self):
        """Get statistics from roll history"""
        if not self.history:
            return None
        
        all_rolls = []
        for roll in self.history:
            all_rolls.extend(roll['results'])
        
        return {
            'total_rolls': len(all_rolls),
            'average': round(sum(all_rolls) / len(all_rolls), 2),
            'min': min(all_rolls),
            'max': max(all_rolls),
            'recent_rolls': len(self.history)
        }

# Global dice simulator instance
dice_sim = DiceSimulator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/roll', methods=['POST'])
def api_roll():
    try:
        data = request.get_json()
        num_dice = int(data.get('num_dice', 1))
        num_sides = int(data.get('num_sides', 6))
        
        result = dice_sim.roll_dice(num_dice, num_sides)
        stats = dice_sim.get_statistics()
        
        return jsonify({
            'success': True,
            'result': result,
            'statistics': stats
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

@app.route('/api/history')
def api_history():
    return jsonify({
        'success': True,
        'history': dice_sim.history[-10:],  # Return last 10 rolls
        'statistics': dice_sim.get_statistics()
    })

@app.route('/api/clear', methods=['POST'])
def api_clear():
    dice_sim.history.clear()
    return jsonify({'success': True, 'message': 'History cleared'})

if __name__ == '__main__':
    app.run(debug=True)