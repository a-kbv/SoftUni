import math

def painting():
    paint_count = int(input())
    wallpaper_count = int(input())
    gloves_price = float(input())
    brush_price = float(input())

    paint_price = 21.50
    wallpaper_price = 5.20
    gloves_count = math.ceil(0.35 * wallpaper_count)
    brushes_count = math.floor(0.48 * paint_count)

    total_paint_price = paint_count * paint_price
    total_wallpapper_price = wallpaper_count * wallpaper_price
    total_gloves_price = gloves_count * gloves_price
    total_beushes_price = brushes_count * brush_price

    total = (total_beushes_price +
             total_gloves_price +
             total_paint_price +
             total_wallpapper_price)

    dellivery_price = ((1/15) * total)

    return f'This delivery will cost {dellivery_price:.2f} lv.'

print(painting())