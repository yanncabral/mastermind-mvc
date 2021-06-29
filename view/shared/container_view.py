def container_view(canvas, *, column, row, color, padding_x=16, padding_y=16, **kwargs):
    i, j, px, py = column, row, padding_x/2, padding_y/2
    return canvas.create_rectangle(
        50 * i + px, 50 * j + py, 
        50 * (i+1) - px,  50 * (j+1) - py, 
        fill=color, 
        outline=color,
        width=2,
        **kwargs
    )
