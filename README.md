
# Car Price Predictor

A Streamlit web application that predicts car prices based on user inputs such as car company, model, year, kilometers driven, and fuel type. The app uses a pre-trained Linear Regression model (`LinearRegressionModel.pkl`) to generate predictions.

## Features
- Interactive UI built with Streamlit
- Select car company, model, year, and fuel type from dropdown menus
- Input kilometers driven
- Predict car price with a single click
- Clean and optimized code with cached data and model loading
- Warning suppression for a smooth user experience

## Prerequisites
- Python 3.8 or higher
- A virtual environment (recommended)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   - `streamlit>=1.38.0`
   - `pandas>=2.2.2`
   - `numpy>=1.26.4`
   - `scikit-learn>=1.5.1`

4. **Ensure Model and Data Files**
   - Place `LinearRegressionModel.pkl` (pre-trained model) in the project root.
   - Place `cleaned.csv` (car data) in the project root.

## Usage

1. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the name of your Python script if different.

2. **Access the App**
   - Open your browser and go to `http://localhost:8501`.
   - Select the car company, model, year, fuel type, and enter kilometers driven.
   - Click **Predict Price** to see the predicted car price.

## Project Structure
```
car-price-predictor/
│
├── app.py                   # Main Streamlit app script
├── LinearRegressionModel.pkl # Pre-trained model
├── cleaned.csv              # Car data file
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

## Notes
- The `LinearRegressionModel.pkl` must be compatible with the `scikit-learn` version installed. If you encounter issues, ensure the model was trained with `scikit-learn>=1.5.1` or update the version in `requirements.txt`.
- The `cleaned.csv` file should contain columns: `name`, `company`, `year`, `kms_driven`, `fuel_type`.
- For deployment (e.g., Streamlit Cloud), ensure all files are included in the repository and `requirements.txt` is in the root.

## Troubleshooting
- **Module Not Found**: Verify all dependencies are installed (`pip install -r requirements.txt`).
- **Model Loading Error**: Check that `LinearRegressionModel.pkl` exists and is not corrupted.
- **Data Error**: Ensure `cleaned.csv` is in the correct format and path.

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.
```
