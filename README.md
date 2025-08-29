# 🎲 Dice Rolling Simulator

A modern, interactive dice rolling simulator built with Flask and deployed on Vercel. Perfect for tabletop gaming, probability experiments, or just having fun!

**Created by Umar J**

## ✨ Features

- 🎯 **Multiple Dice Types**: Support for D4, D6, D8, D10, D12, D20, and D100
- 🔢 **Multiple Dice**: Roll up to 10 dice simultaneously
- 📊 **Real-time Statistics**: Track averages, min/max values, and roll counts
- 📝 **Roll History**: Keep track of your recent rolls
- 🎨 **Beautiful UI**: Modern, responsive design with smooth animations
- 📱 **Mobile Friendly**: Works perfectly on all device sizes
- ⚡ **Fast & Reliable**: Optimized for quick response times

## 🚀 Live Demo

[View Live Demo]([[https://your-app-name.vercel.app)]

## 🛠️ Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel
- **Styling**: Custom CSS with modern design principles

## 📋 Prerequisites

- Python 3.7+
- pip (Python package installer)
- Vercel account (for deployment)

## 🔧 Installation & Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dice-rolling-simulator.git
cd dice-rolling-simulator
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Locally

```bash
python app.py
```

Visit `http://localhost:5000` in your browser to see the application running locally.

## 🌐 Deploy to Vercel

### Method 1: Deploy with Vercel CLI (Recommended)

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Set up and deploy? `Yes`
   - Which scope? Choose your account
   - Link to existing project? `No`
   - Project name? `dice-rolling-simulator` (or your preferred name)
   - In which directory is your code located? `./`

### Method 2: Deploy with GitHub Integration

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/dice-rolling-simulator.git
   git push -u origin main
   ```

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the Flask app and deploy it

## 📁 Project Structure

```
dice-rolling-simulator/
│
├── app.py                 # Main Flask application with API endpoints
├── requirements.txt       # Python dependencies (Flask)
├── vercel.json           # Vercel deployment configuration
├── templates/
│   └── index.html        # Main HTML template with CSS and JavaScript
└── README.md             # This file
```

## 🎮 How to Use

1. **Select Dice Configuration**:
   - Choose the number of dice (1-10)
   - Select dice type (D4, D6, D8, D10, D12, D20, D100)

2. **Roll the Dice**:
   - Click the "🎲 Roll Dice!" button
   - Watch the animated dice results

3. **View Results**:
   - See individual dice values
   - Check the total sum
   - Review statistics and roll history

4. **Track Performance**:
   - Monitor your rolling statistics
   - View recent roll history
   - Clear history when needed

## 🔗 API Endpoints

### POST `/api/roll`
Roll dice with specified parameters.

**Request Body**:
```json
{
  "num_dice": 2,
  "num_sides": 6
}
```

**Response**:
```json
{
  "success": true,
  "result": {
    "dice": 2,
    "sides": 6,
    "results": [4, 6],
    "total": 10
  },
  "statistics": {
    "total_rolls": 12,
    "average": 7.5,
    "min": 2,
    "max": 12,
    "recent_rolls": 6
  }
}
```

### GET `/api/history`
Get recent roll history and statistics.

### POST `/api/clear`
Clear roll history.

## 🎨 Customization

### Changing Dice Limits
Edit the validation in `app.py`:
```python
if num_dice < 1 or num_dice > 10:  # Change max dice here
if num_sides < 2 or num_sides > 100:  # Change max sides here
```

### Adding New Dice Types
Add options to the `numSides` select in `templates/index.html`:
```html
<option value="30">D30</option>
```

### Styling Changes
Modify the CSS in `templates/index.html` to match your preferred color scheme and design.

## 🧪 Testing

### Manual Testing Checklist
- [ ] Roll single die (D6)
- [ ] Roll multiple dice (2-10)
- [ ] Test different dice types (D4, D8, D10, D12, D20, D100)
- [ ] Verify total calculation
- [ ] Check statistics accuracy
- [ ] Test history functionality
- [ ] Clear history feature
- [ ] Error handling (invalid inputs)
- [ ] Mobile responsiveness

### API Testing with cURL
```bash
# Roll 2 D6 dice
curl -X POST http://localhost:5000/api/roll \
  -H "Content-Type: application/json" \
  -d '{"num_dice": 2, "num_sides": 6}'

# Get history
curl http://localhost:5000/api/history

# Clear history
curl -X POST http://localhost:5000/api/clear
```

## 🐛 Troubleshooting

### Common Issues

1. **Vercel Deployment Fails**:
   - Ensure `vercel.json` is in the root directory
   - Check that `requirements.txt` contains Flask
   - Verify Python version compatibility

2. **Flask App Won't Start**:
   - Check if Flask is installed: `pip list | grep Flask`
   - Ensure you're in the correct directory
   - Check for syntax errors in `app.py`

3. **Static Files Not Loading**:
   - Ensure templates folder exists
   - Check file paths in Flask routes

## 📈 Future Enhancements

- 🎲 Custom dice faces/symbols
- 📊 Advanced statistics (standard deviation, frequency charts)
- 💾 Persistent user sessions
- 🎵 Sound effects for dice rolls
- 🌙 Dark/Light mode toggle
- 📤 Export roll history
- 🎯 Dice roll modifiers (+1, -1, advantage/disadvantage)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Commit your changes: `git commit -m "Add feature"`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 About the Creator

**Umar J** - Passionate developer creating useful and fun applications.

- 🌐 Portfolio: [Add your portfolio URL]
- 💼 LinkedIn: [Add your LinkedIn]
- 🐦 Twitter: [Add your Twitter]
- 📧 Email: [Add your email]

## 🙏 Acknowledgments

- Thanks to the Flask community for the excellent framework
- Vercel for providing seamless deployment
- All the tabletop gaming community for inspiration

---

⭐ **Star this repository if you found it helpful!**

Made with ❤️ by **Umar J**
