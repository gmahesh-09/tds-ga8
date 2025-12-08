"""
Interactive Data Analysis Notebook
Research Institution - Data Science Department
Email: 24ds2000081@ds.study.iitm.ac.in

This Marimo notebook demonstrates the relationship between variables
in a dataset with interactive visualizations and dynamic outputs.
"""

import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    Cell 1: Import Dependencies and Setup
    
    This cell imports all necessary libraries for data analysis.
    No dependencies on other cells.
    
    Data flow: None (entry point)
    Email: 24ds2000081@ds.study.iitm.ac.in
    """
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Display header
    mo.md("""
    # Interactive Data Analysis Dashboard
    
    **Research Institution - Data Science Lab**  
    **Email:** 24ds2000081@ds.study.iitm.ac.in
    
    This notebook demonstrates interactive data exploration with variable dependencies.
    """)
    return mo, np, pd, plt


@app.cell
def __(mo):
    """
    Cell 2: Create Interactive Slider Widget
    
    This cell defines the interactive slider that controls sample size.
    Depends on: marimo (mo) from Cell 1
    
    Data flow: Cell 1 (mo) → Cell 2 (slider) → Cell 3, Cell 4, Cell 5
    """
    # Interactive slider for sample size
    # Range: 50 to 1000 samples
    # This widget will trigger re-execution of dependent cells
    sample_size_slider = mo.ui.slider(
        start=50,
        stop=1000,
        step=50,
        value=200,
        label="Sample Size (n):",
        show_value=True
    )
    
    sample_size_slider
    return sample_size_slider,


@app.cell
def __(sample_size_slider, np, pd):
    """
    Cell 3: Generate Synthetic Dataset
    
    This cell generates synthetic data based on the slider value.
    Depends on: sample_size_slider from Cell 2, np and pd from Cell 1
    
    Data flow: Cell 1 (np, pd) + Cell 2 (slider) → Cell 3 (dataset) → Cell 4, Cell 5
    
    The dataset simulates a relationship between study hours and exam scores
    with some random noise to make it realistic.
    """
    # Get current sample size from slider
    n_samples = sample_size_slider.value
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate synthetic data: relationship between study hours and exam scores
    # Linear relationship with noise
    study_hours = np.random.uniform(0, 10, n_samples)
    
    # Exam score = 50 + 4 * study_hours + noise
    # This creates a positive correlation
    noise = np.random.normal(0, 5, n_samples)
    exam_scores = 50 + 4 * study_hours + noise
    
    # Clip scores to realistic range [0, 100]
    exam_scores = np.clip(exam_scores, 0, 100)
    
    # Create DataFrame
    dataset = pd.DataFrame({
        'study_hours': study_hours,
        'exam_scores': exam_scores,
        'student_id': range(1, n_samples + 1)
    })
    
    # Calculate statistics for use in other cells
    correlation = dataset['study_hours'].corr(dataset['exam_scores'])
    mean_score = dataset['exam_scores'].mean()
    std_score = dataset['exam_scores'].std()
    
    dataset
    return dataset, correlation, mean_score, std_score, n_samples, study_hours, exam_scores, noise


@app.cell
def __(mo, dataset, correlation, mean_score, std_score, n_samples):
    """
    Cell 4: Dynamic Markdown Output Based on Widget State
    
    This cell generates markdown output that changes based on slider value.
    Depends on: mo from Cell 1, dataset variables from Cell 3
    
    Data flow: Cell 1 (mo) + Cell 3 (stats) → Cell 4 (dynamic markdown)
    
    The markdown content is dynamically generated based on:
    - Current sample size (from slider)
    - Calculated correlation coefficient
    - Statistical measures (mean, std)
    """
    # Dynamic markdown that updates when slider changes
    dynamic_output = mo.md(f"""
    ## 📊 Dataset Statistics
    
    **Current Sample Size:** {n_samples} students  
    Email: 24ds2000081@ds.study.iitm.ac.in
    
    ### Correlation Analysis
    
    - **Pearson Correlation Coefficient:** {correlation:.4f}
    - **Interpretation:** {"Strong positive" if correlation > 0.7 else "Moderate positive" if correlation > 0.4 else "Weak positive"} relationship
    
    ### Exam Score Distribution
    
    - **Mean Score:** {mean_score:.2f}
    - **Standard Deviation:** {std_score:.2f}
    - **Range:** [{dataset['exam_scores'].min():.2f}, {dataset['exam_scores'].max():.2f}]
    
    ### Key Insights
    
    {f"✅ With {n_samples} samples, we observe a {correlation:.2f} correlation between study hours and exam scores." if n_samples >= 100 else f"⚠️ Sample size of {n_samples} may be too small for reliable conclusions."}
    
    {"🎯 **Recommendation:** Students who study more hours tend to achieve higher exam scores." if correlation > 0.5 else "📌 **Note:** Consider other factors that might influence exam performance."}
    """)
    
    dynamic_output
    return dynamic_output,


@app.cell
def __(dataset, plt, n_samples, correlation):
    """
    Cell 5: Visualization with Dependent Variables
    
    This cell creates scatter plot visualization.
    Depends on: dataset from Cell 3, plt from Cell 1
    
    Data flow: Cell 1 (plt) + Cell 3 (dataset) → Cell 5 (visualization)
    
    The plot updates automatically when the slider changes because
    it depends on the dataset variable which is recalculated in Cell 3.
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot
    ax.scatter(
        dataset['study_hours'], 
        dataset['exam_scores'],
        alpha=0.6,
        color='steelblue',
        edgecolors='black',
        s=50
    )
    
    # Add regression line
    z = np.polyfit(dataset['study_hours'], dataset['exam_scores'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(dataset['study_hours'].min(), dataset['study_hours'].max(), 100)
    ax.plot(x_line, p(x_line), "r--", linewidth=2, label=f'Linear fit (r={correlation:.3f})')
    
    # Labels and title
    ax.set_xlabel('Study Hours per Week', fontsize=12, fontweight='bold')
    ax.set_ylabel('Exam Score (0-100)', fontsize=12, fontweight='bold')
    ax.set_title(f'Relationship between Study Hours and Exam Scores (n={n_samples})', 
                 fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Set axis limits
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(0, 105)
    
    plt.tight_layout()
    fig
    return fig, ax, z, p, x_line


@app.cell
def __(mo, dataset):
    """
    Cell 6: Interactive Data Table
    
    This cell displays the first 10 rows of the dataset.
    Depends on: mo from Cell 1, dataset from Cell 3
    
    Data flow: Cell 1 (mo) + Cell 3 (dataset) → Cell 6 (table display)
    
    The table automatically updates when the slider changes because
    the dataset is regenerated in Cell 3.
    """
    mo.md(f"""
    ## 📋 Sample Data (First 10 Rows)
    
    Below is a preview of the generated dataset. The full dataset contains {len(dataset)} observations.
    """)
    return


@app.cell
def __(dataset):
    """
    Cell 7: Display Dataset Preview
    
    Depends on: dataset from Cell 3
    Data flow: Cell 3 (dataset) → Cell 7 (display)
    """
    # Display first 10 rows
    dataset.head(10)
    return


@app.cell
def __(mo, n_samples, correlation):
    """
    Cell 8: Additional Analysis and Recommendations
    
    This cell provides conditional recommendations based on the data.
    Depends on: mo from Cell 1, statistics from Cell 3
    
    Data flow: Cell 1 (mo) + Cell 3 (n_samples, correlation) → Cell 8 (recommendations)
    """
    # Generate recommendations based on current state
    recommendations = []
    
    if n_samples < 100:
        recommendations.append("📈 **Increase sample size** to at least 100 for more reliable results")
    
    if correlation > 0.7:
        recommendations.append("✨ **Strong correlation detected** - Study hours are a strong predictor of exam performance")
    elif correlation > 0.4:
        recommendations.append("📊 **Moderate correlation found** - Study hours influence exam scores but other factors may also play a role")
    else:
        recommendations.append("🔍 **Weak correlation** - Consider investigating additional variables that affect exam performance")
    
    if n_samples >= 500:
        recommendations.append("✅ **Large sample size** - Statistical results are highly reliable")
    
    rec_text = "\n".join([f"- {rec}" for rec in recommendations])
    
    mo.md(f"""
    ## 💡 Recommendations
    
    Based on the current analysis with {n_samples} samples:
    
    {rec_text}
    
    ---
    
    **For further analysis or questions, ** Email: 24ds2000081@ds.study.iitm.ac.in
    """)
    return recommendations, rec_text


@app.cell
def __(mo):
    """
    Cell 9: Usage Instructions
    
    This cell provides instructions for interacting with the notebook.
    Depends on: mo from Cell 1
    
    Data flow: Cell 1 (mo) → Cell 9 (instructions)
    """
    mo.md("""
    ---
    
    ## 🎮 How to Use This Notebook
    
    1. **Adjust the slider** above to change the sample size (50-1000)
    2. **Observe** how all dependent cells automatically update:
       - Statistics recalculate
       - Visualization redraws
       - Markdown content regenerates
       - Recommendations adjust
    3. **Experiment** with different sample sizes to see how correlation stability changes
    
    ### Variable Dependencies Flow Chart
    
    ```
    Cell 1: Imports (mo, np, pd, plt)
       ↓
    Cell 2: Slider Widget (sample_size_slider)
       ↓
    Cell 3: Generate Dataset (dataset, correlation, mean_score, etc.)
       ↓
    Cell 4: Dynamic Markdown (dynamic_output)
    Cell 5: Visualization (scatter plot + regression)
    Cell 6-7: Data Table Display
    Cell 8: Recommendations
    ```
    
    **Notebook Author:** Data Science Department  
    **Email:** 24ds2000081@ds.study.iitm.ac.in 
    **Framework:** Marimo (Reactive Python Notebooks)
    """)
    return


if __name__ == "__main__":
    app.run()
