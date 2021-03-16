import plotly.graph_objects as go
import math

men = [37.9, 46.5, 37.6, 25.6]
women = [35.4, 43.3, 37.8, 22.7]
total = [36.6, 44.9, 37.7, 24.1]

age_range=["Over 20", "20-39", "40-59", "Over 60"]

figure = go.Figure()

figure.add_trace(
    go.Bar(
        x = age_range, 
        y = men, 
        name = 'Men',
        marker_color = 'orange'
    )
)

figure.add_trace(
    go.Bar(
        x = age_range, 
        y = women, 
        name = 'Women',
        marker_color = 'red'
    )
)

figure.add_trace(
    go.Bar(
        x = age_range, 
        y = total, 
        name = 'Total',
        marker_color = 'green'
    )
)

figure.update_layout(
    title_text = 'Exponential Graphs', 
    title_font_color = 'blue', 
    title_font_family = 'Times New Roman',
    title_font_size = 32,

    yaxis = dict(
        title = 'Output Value',
        titlefont_size = 24,
        title_font_color = 'blue', 
        title_font_family = 'Times New Roman',
    ),

    xaxis = dict(
        title = 'Age Ranges',
        titlefont_size = 24,
        title_font_color = 'blue', 
        title_font_family = 'Times New Roman',
    ),
    
    barmode = 'group'
)

figure.show()